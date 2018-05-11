import pandas as pd
import numpy as np
import sys
import os.path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import operator
from sklearn import decomposition
import matplotlib
import matplotlib.pyplot as plt

def rank_terms( A, terms ):
    # get the sums over each column
    sums = A.sum(axis=0)
    # map weights to the terms
    weights = {}
    for col, term in enumerate(terms):
        weights[term] = sums[0,col]
    # rank the terms by their weight over all documents
    return sorted(weights.items(), key=operator.itemgetter(1), reverse=True)

def get_descriptor( terms, H, topic_index, top ):
    # reverse sort the values to sort the indices
    top_indices = np.argsort( H[topic_index,:] )[::-1]
    # now get the terms corresponding to the top-ranked indices
    top_terms = []
    for term_index in top_indices[0:top]:
        top_terms.append( terms[term_index] )
    return top_terms

def plot_top_term_weights( terms, H, topic_index, top, filter_type, keyword, topic_count):
    # get the top terms and their weights
    top_indices = np.argsort( H[topic_index,:] )[::-1]
    top_terms = []
    top_weights = []
    for term_index in top_indices[0:top]:
        top_terms.append( terms[term_index] )
        top_weights.append( H[topic_index,term_index] )
    # note we reverse the ordering for the plot
    top_terms.reverse()
    top_weights.reverse()
    # create the plot
    fig = plt.figure(figsize=(13,8))
    # add the horizontal bar chart
    ypos = np.arange(top)
    ax = plt.barh(ypos, top_weights, align="center", color="green",tick_label=top_terms)
    plt.xlabel("Term Weight",fontsize=14)
    plt.tight_layout()
    plt.title("Word distribution for topic " + str(topic_index+1))
    name = 'result_' + filter_type + '_' + keyword + '_' + str(topic_index+1) + '-' + str(topic_count) + '.png'
    plt.savefig(name, bbox_inches='tight')
    #plt.show()

def run_lyrics(filter_type, keyword, topic_count):
    if (topic_count < 1):
        print ("topic_count must be greater than 0")
        return None
    if filter_type != 'year' and filter_type != 'artist' and filter_type != 'genre':
        print("filter_type is not 'artist', 'year' or 'genre'")
        #print("no such type word, please enter <artist> or <year> or <genre>")
        return None
    keyword_str = keyword
    if filter_type == 'year':
        keyword = int(keyword)
    print("loading database...")
    df = pd.read_csv('lyrics_cleanup.csv')
    df = df.dropna(axis=0, how='any')
    df1 = df[['index','song', filter_type, 'lyrics']]
    df2 = df1[df1[filter_type] == keyword]
    if df2.empty:
        print("Second argument is not a valid keyword")
        return None
    print("done")
    print("calculating...")
    raw_documents = []
    for index, row in df2.iterrows():
        if row['lyrics'] != np.nan:
            raw_documents.append(row['lyrics'])
    custom_stop_words = []
    with open( "lemur-stopwords.txt", "r" ) as fin:
        for line in fin.readlines():
            custom_stop_words.append(line.strip())
    vectorizer = CountVectorizer(stop_words = custom_stop_words, min_df = 20)
    A = vectorizer.fit_transform(raw_documents)
    terms = vectorizer.get_feature_names()
    vectorizer = TfidfVectorizer(stop_words=custom_stop_words, min_df = 20)
    A = vectorizer.fit_transform(raw_documents)
    terms = vectorizer.get_feature_names()
    print("done")

    ranking = rank_terms(A, terms)
    name = 'result_top_20_words_' + filter_type + '_' + keyword_str + '_' + str(topic_count) + '.txt'
    print("writing top 20 words...")
    f1 = open(name,"w+")
    f1.write("Top 20 words for searching " + filter_type + " " + keyword_str + " " + str(topic_count) +"\n")
    for i, pair in enumerate( ranking[0:20] ):
        f1.write("\n%02d. %s (%.2f)" % (i+1, pair[0], pair[1]))
        #print( "%02d. %s (%.2f)" % (i+1, pair[0], pair[1]))
    f1.close()
    print("done")
    
    k = topic_count
    model = decomposition.NMF( init="nndsvd", n_components=k ) 
    # apply the model and extract the two factor matrices
    W = model.fit_transform( A )
    H = model.components_
    descriptors = []
    name = 'result_topic_list_' + filter_type + '_' + keyword_str + '_' + str(topic_count) + '.txt'
    print("writing topic list...")
    f2 = open(name,"w+")
    f2.write("Topic list for searching " + filter_type + " " + keyword_str + " " + str(topic_count) +"\n")
    for topic_index in range(k):
        descriptors.append( get_descriptor( terms, H, topic_index, 10 ) )
        str_descriptor = ", ".join( descriptors[topic_index] )
        #print("Topic %02d: %s" % ( topic_index+1, str_descriptor ) )
        f2.write("\nTopic %02d: %s" % ( topic_index+1, str_descriptor ))
    f2.close()
    print("done")
    print("outputting graphs...")
    plt.style.use("ggplot")
    matplotlib.rcParams.update({"font.size": 14})
    for i in range(topic_count):
    	plot_top_term_weights( terms, H, i, 15, filter_type, keyword_str, topic_count)
    	print("outputting graph " + str(i+1) + "/" + str(topic_count))
    print("done")
    print("have a nice day :)")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Please specify the following 3 parameters: filter_type, keyword, topic_count")
        sys.exit(1)
    else:
        filter_type = sys.argv[1]
        keyword = sys.argv[2]
        topic_count = int(sys.argv[3])
        run_lyrics(filter_type, keyword, topic_count)
