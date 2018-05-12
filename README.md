# Lyrics

This is the repository for CS410 course project - peiyaol2, pj2, xinyigu2

Our main goal is to do topic modeling on the lyrics database given some specific query input.

## Getting started
*Important*: please log onto google drive with your illinois account and [download our database](https://drive.google.com/file/d/1g8SArnDU4XOSbdUIZvQ1-glQ5cJnFOlF/view?usp=sharing), then put the unzipped csv file in the program directory.

Please also read through the [installing packages section below](https://github.com/peiyaoli2/Lyrics#installing-packages) before running our program.

To run our program, navigate to the project directory and run
```
python lyrics.py <filter_type> <keyword> <topic_count>
```

### Meaning of parameters
#### filter_type
is the type of filter you want to search for. There are three valid arguments for this parameter: artist, genre or year.

#### keyword
is either the name of the artist, the name of the genre or the year you want to search for.
For a complete list of valid arguments, please look at
* [valid_artist.txt](https://github.com/peiyaoli2/Lyrics/blob/master/valid_artist.txt)
* [valid_genre.txt](https://github.com/peiyaoli2/Lyrics/blob/master/valid_genre.txt)
* [valid_year.txt](https://github.com/peiyaoli2/Lyrics/blob/master/valid_year.txt)

inside our repository.

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
There are several helper functions and a main function in our program.

### rank_terms
This is a helper function.
### get_descriptor
This is a helper function.
### plot_top_term_weights
This is a helper function.
### run_lyrics
This is the main function.

## Contributors
* Peiyao Li (peiyaol2)
* Peiwen Jiang (pj2)
* Xinyi Gu (xinyigu2)

## Resources
* [Here](https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics) is the lyrics database we used to do our topic modeling from. Note that we cleaned up the database by removing empty values and keywords that only appear once in the database, because we cannot do topic modeling on those keywords.
* [Here](https://github.com/derekgreene/topic-model-tutorial) is a topic modeling tutorial that we used to accomplish our project.
