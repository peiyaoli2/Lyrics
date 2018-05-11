# Lyrics

This is the repository for CS410 course project - peiyaol2, pj2, xinyigu2
Our main goal is to do topic modeling on the lyrics database given some specific parameters.

## Getting started
To run our program, navigate to the project directory and run
```
python lyrics.py <filter_type> <filter_name> <topic_count>
```

### Meaning of parameters
<filter_type> is the type of filter you want to search for. There are three valid arguments for this parameter: artist, genre or year.

<filter_name> is either the name of the artist, the name of the genre or the name of the year you want to search for.
For a complete list of valid arguments, please look at
```
valid_artist.txt valid_genre.txt valid_year.txt
```

<topic_count> is the number of topic you want to search for.
  
### Example run
For example, to search for backstreet boys for 5 topics, you can run our program with
```
python lyrics.py artist backstreet-boys 5
```

To search for the pop genre with 10 topics, you can run our program with
```
python lyrics.py genre Pop 10
```

To search for year 2008 with 8 topics, you can run our program with
```
python lyrics.py year 2008 8
```
