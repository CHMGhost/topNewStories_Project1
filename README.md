# Background of Application
This project uses combination of items

* Python

* Streamlit

* New York Times API

* JSON

## <ins>Overview<ins>
My professor tasked me with creating a web application that uses Python, the Streamlit platform, the API from the New York Times, and JSON documents.

## <ins>Packages used</ins>
* Streamlit
* nltk
* request
* wordcloud
* pylot

```
pip3 install streamlit nltk requests pylot
```
For wordcloud
We used anaconda
```
conda install -c https://conda.anaconda.org/conda-forge wordcloud
```

## <ins>First section</ins>
In the first section of the application. The user is asked for their name and preferred topic of news.

When the user has enter their name and selected a topic. This will display two checkboxes for the following<br>
1. Frequency distribution for the top 10 most common words used in the top stories.
2. A Wordcloud image of the top 10 most common words used.


## <ins>Second Section</ins>
In the second section of the application. The user is asked for their preferred set of articles. They can choose from the following.<br>
1. Shared
2. Emailed
3. Viewed
   
The user is also asked for their preffered the maximum age of articles. They can choose from the following.<br>
1. 1 day
2. 7 days
3. 30 days

Once the users has made their selections a wordcloud image will be displayed.

### <ins>Question</ins>
Please send me an email at keithminork@gmail.com