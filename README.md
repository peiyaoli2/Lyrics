# Topic Modeling on Lyrics

This is the repository for CS410 course project - peiyaol2, pj2, xinyigu2

This program runs on the command line and does topic modeling on the lyrics database given some specific query input.

## Getting started
*Important*: please log onto google drive with your illinois account and [download our database](https://drive.google.com/file/d/1g8SArnDU4XOSbdUIZvQ1-glQ5cJnFOlF/view?usp=sharing), then put the unzipped csv file in the project directory.

Please also read through the [installing packages section below](https://github.com/peiyaoli2/Lyrics#installing-packages) before running our program.

To run our program, navigate to the project directory and run
```
python lyrics.py <filter_type> <keyword> <topic_count>
```

### Meaning of parameters
#### filter_type
is the type of filter you want to search for. There are three valid arguments for this parameter: *artist*, *genre* or *year*.

#### keyword
is either the name of the artist, the name of the genre or the year you want to search for.
For a complete list of valid keywords, please look at
* [valid_artist_with_frequency.txt](https://github.com/peiyaoli2/Topic-Modeling-on-Lyrics/blob/master/valid_artist_with_frequency.txt)
* [valid_genre.txt](https://github.com/peiyaoli2/Lyrics/blob/master/valid_genre.txt)
* [valid_year.txt](https://github.com/peiyaoli2/Lyrics/blob/master/valid_year.txt)

inside our repository. Note that we excluded artist with frequency lower than 20.

#### topic_count
is the number of topic you want to search for.
  
### Example runs
* To search for backstreet boys for 5 topics, you can run our program with
  ```
  python lyrics.py artist backstreet-boys 5
  ```

* To search for the pop genre with 10 topics, you can run our program with
  ```
  python lyrics.py genre Pop 10
  ```

* To search for year 2008 with 8 topics, you can run our program with
  ```
  python lyrics.py year 2008 8
  ```

### Interpreting the output
Upon completion of the program, several output will appear inside the program directory.
#### top 20 words
This is the list of the top 20 words ranked by the frequency of appearance with your input parameter. It appears as a .txt file.
#### topic list
This is the list of topics of your specified count. It appears as a .txt file.
#### word distribution for each topic
These are several images demonstrating the word distribution of each topic in the topic list. The amount of images varies base on your input topic_count. They appear as .png files.

## Installing packages
Here are a few packages that should be installed before running the program:
* [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)
* [numpy](https://docs.scipy.org/doc/numpy-1.14.0/user/install.html)
* [scikit-learn](http://scikit-learn.org/stable/install.html)
* [matplotlib](https://matplotlib.org/users/installing.html)

## Implementation
There are several helper functions and a main function in our program. Note that there are also comments inside the source file.

### rank_terms
This is a helper function. It helps us look at the terms with the highest TF-IDF scores across all documents in the document-term matrix and rank the terms by their weight.
### get_descriptor
This is a helper function. It extracts the descriptor for a specified topic. The topic descriptor are the top ranked terms from the H factor for each topic.
### plot_top_term_weights
This is a helper function. It creates a bar chart for the specified topic with matplotlib.pyplot, based on the H factor from the current NMF model.
### run_lyrics
This is the main function. It has several components:
* First, it loads the database and checks the input parameter with the database. If input is not valid, it returns None.
* Then, it creates a vector of lyrics, accounting for stopwords and TF-IDF weightings.
* Then, it creates a document-term matrix and rank the terms using the helper function.
* Next, it does NMF decomposition on the lyrics matrix.
* Lastly, it outputs our desired top terms and topic list, as well as bar graphs.

## Contributors
* Peiyao Li (peiyaol2)

  Came up with ideas about the project and designed the outline for the project. Followed the tutorial and wrote a majority part of the source code (lyrics.py and valid_artist_with_frequency.txt) with teammates' help. Wrote a large portion of the readme file. Voiced the video presentation.
* Peiwen Jiang (pj2)
  
  Generated the valid_year.txt, valid_genre.txt, valid_artist.txt(a previous version of valid_artist_with_frequency.txt) based on the database using python. Found some tutorial   websites to help teammates start the project. Completed the video editing and published in the media. 
* Xinyi Gu (xinyigu2)

  Found some resources websites for the project. Tried different methods to do topic modeling. Helpped debug the code for different versions of the project. 

## Resources
* [Here](https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics) is the lyrics database we used to do our topic modeling from. Note that we cleaned up the database by removing empty values and keywords that only appear once in the database, because we cannot do topic modeling on those keywords.
* [Here](https://github.com/derekgreene/topic-model-tutorial) is a topic modeling tutorial that we used to accomplish our project. We have followed part 1 and part 2 for this project.
