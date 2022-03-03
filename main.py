import streamlit as st
import main_functions
import requests
import nltk
from datetime import date, time
import pandas as pd
import numpy as np
import time as tm
import pydeck as pdk
import plotly.express as px
import matplotlib.pyplot as plt
from nltk import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Streamlit set up
st.set_page_config(
    page_title='COP 4813 - Web Application Programming - Project 1',
    layout='wide'
)

st.title("Project 1")
st.header("Part A - The Top Stories API")
st.text("This app uses the top stories api to display the most common words used in the top current"
        "\narticles based on a specified topic selected by the user. The data is displayed as a line chart"
        "\nand as a wordcloud image.")

add_inputbox = st.text_input(
    "Please enter your name"
)
add_selectionbox = st.selectbox(
    "Select a topic of your interest",
    ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine",
     "movies", "nyregion", "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview",
     "technology", "theater", "t-magazine", "travel", "upshot", "us", "world"]
)

# Downloads the latest news
api_key_dict = main_functions.read_from_file("JSON/api_key.json")
apy_key = api_key_dict['my_key']
url = "https://api.nytimes.com/svc/topstories/v2/" + add_selectionbox + ".json?api-key=" + apy_key
response = requests.get(url).json()
main_functions.save_to_file(response, "JSON/response.json")
my_articles = main_functions.read_from_file("JSON/response.json")

# Finding the abstract
str1 = ""
for my_article in my_articles["results"]:
    str1 = str1 + my_article["abstract"]
# Displays sentences
sentences = sent_tokenize(str1)
# Gets text as words
my_words = word_tokenize(str1)
# Displays freq of words in text
fdist = FreqDist(my_words)
words_no_punc = []

for my_word in my_words:
    if my_word.isalpha():
        words_no_punc.append(my_word.lower())
stopwords = stopwords.words('english')
clean_words = []

for word_no_punc in words_no_punc:
    if word_no_punc not in stopwords:
        clean_words.append(word_no_punc)
fdist2 = FreqDist(clean_words)
fdist3 = fdist2.most_common(10)


# User must add their name and select a topic
if add_inputbox and add_selectionbox:
    st.text("Hi, " + add_inputbox + " you have select the " + add_selectionbox + " topic.")

    # Display the frequency distribution of words
    st.subheader("II - Frequency Distribution")
    freq_box = st.checkbox("Click here to generate frequency distribution")
    if freq_box:
        df = pd.DataFrame(
            fdist3,
            columns=['Words', 'Count'],
        )
        df=df.rename(columns={'Words':'index'}).set_index('index')
        st.line_chart(df)

    # Display a wordcloud of the 10 top most common words
    st.subheader("III - Wordcloud")
    wordcloud_box = st.checkbox("Click here to generate wordcloud")

    if wordcloud_box:
        # Creates word cloud
        st.set_option('deprecation.showPyplotGlobalUse', False)
        wordCloud = WordCloud().generate(str1)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

#Part 2 of project 1
st.header("Part B Most Popular Articles")
st.text("Select if you want to see the most shared, emailed, or viewed articles.")

# Display the user's preferred set of articles
preferred_articles = st.multiselect(
    "Select your preferred set of articles.",
    ["most shared", "emailed", "viewed articles"]
)

time_period = st.multiselect(
    "Select the period of time (last days)",
    ["1", "7", "30"]
)

if preferred_articles and time_period:
    # Creates word cloud
    st.set_option('deprecation.showPyplotGlobalUse', False)
    wordCloud = WordCloud().generate(str1)
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()
