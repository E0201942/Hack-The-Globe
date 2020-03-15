import pickle
from ColumnExtract import ColumnExtract
import numpy as np 
import pandas as pd 
pd.set_option('display.max_colwidth', -1)
from time import time
import pickle
import numpy
import re
import string
import os
import emoji
from pprint import pprint
import collections
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
sns.set(font_scale=1.3)
from sklearn.base import BaseEstimator, TransformerMixin
from ColumnExtract import ColumnExtract
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import gensim
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import warnings
import praw
from praw.models import MoreComments
import sys
import nltk # Imports the library
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
def getData(filname):
    final = []
    for line in open(filname, encoding='utf-8'):
        try:
            final.append(line)
        except:
            continue
    return final
class TextCounts(BaseEstimator, TransformerMixin):
    
    def count_regex(self, pattern, tweet):
        return len(re.findall(pattern, tweet))
    
    def fit(self, X, y=None, **fit_params):
        # fit method is used when specific operations need to be done on the train data, but not on the test data
        return self
    
    def transform(self, X, **transform_params):
        count_words = X.apply(lambda x: self.count_regex(r'\w+', x)) 
        count_mentions = X.apply(lambda x: self.count_regex(r'@\w+', x))
        count_hashtags = X.apply(lambda x: self.count_regex(r'#\w+', x))
        count_capital_words = X.apply(lambda x: self.count_regex(r'\b[A-Z]{2,}\b', x))
        count_excl_quest_marks = X.apply(lambda x: self.count_regex(r'!|\?', x))
        count_urls = X.apply(lambda x: self.count_regex(r'http.?://[^\s]+[\s]?', x))
        # We will replace the emoji symbols with a description, which makes using a regex for counting easier
        # Moreover, it will result in having more words in the tweet
        count_emojis = X.apply(lambda x: emoji.demojize(x)).apply(lambda x: self.count_regex(r':[a-z_&]+:', x))
        
        df = pd.DataFrame({'count_words': count_words
                           , 'count_mentions': count_mentions
                           , 'count_hashtags': count_hashtags
                           , 'count_capital_words': count_capital_words
                           , 'count_excl_quest_marks': count_excl_quest_marks
                           , 'count_urls': count_urls
                           , 'count_emojis': count_emojis
                          })
        
        return df
class CleanText(BaseEstimator, TransformerMixin):
    def remove_mentions(self, input_text):
        return re.sub(r'@\w+', '', input_text)
    
    def remove_urls(self, input_text):
        return re.sub(r'http.?://[^\s]+[\s]?', '', input_text)
    
    def emoji_oneword(self, input_text):
        # By compressing the underscore, the emoji is kept as one word
        return input_text.replace('_','')
    
    def remove_punctuation(self, input_text):
        # Make translation table
        punct = string.punctuation
        trantab = str.maketrans(punct, len(punct)*' ')  # Every punctuation symbol will be replaced by a space
        return input_text.translate(trantab)
    def remove_digits(self, input_text):
        return re.sub('\d+', '', input_text)
    
    def to_lower(self, input_text):
        return input_text.lower()
    
    def remove_stopwords(self, input_text):
        stopwords_list = stopwords.words('english')
        # Some words which might indicate a certain sentiment are kept via a whitelist
        whitelist = ["n't", "not", "no"]
        words = input_text.split() 
        clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1] 
        return " ".join(clean_words) 
    
    def stemming(self, input_text):
        porter = PorterStemmer()
        words = input_text.split() 
        stemmed_words = [porter.stem(word) for word in words]
        return " ".join(stemmed_words)
    
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X, **transform_params):
        clean_X = X.apply(self.remove_mentions).apply(self.remove_urls).apply(self.emoji_oneword).apply(self.remove_punctuation).apply(self.remove_digits).apply(self.to_lower).apply(self.remove_stopwords).apply(self.stemming)
        return clean_X
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
reddit = praw.Reddit(client_id='8kg9KlNRP5EvDA', client_secret='haGhQGP7wEJVhlQ1dIvU0G2wVB8', user_agent='reddit_webscapting')
keywords = None
companies = ["Nestle", "Johnson & Johnson", "Proctor & Gamble", "Pepsi", "Unilever", "AB InBev", "Coca Cola", "JBS", "Phillip Morris", "L'Oreal", "Kellogg"]
companiescsv = ["Nestle.csv", "Johnson & Johnson.csv", "Proctor & Gamble.csv", "Pepsi.csv", "Unilever.csv", "AB InBev.csv", "Coca Cola.csv", "JBS.csv", "Phillip Morris.csv", "L'Oreal.csv", "Kellogg.csv"]
companiescsvc = ["Nestledc.csv", "Johnson & Johnsonc.csv", "Proctor & Gamblec.csv", "Pepsic.csv", "Unileverc.csv", "AB InBevc.csv", "Coca Colac.csv", "JBSc.csv", "Phillip Morrisc.csv", "L'Orealc.csv", "Kelloggc.csv"]

words = []
phrases = []
phraseLength = 2
i = 0
ct = CleanText()
tc = TextCounts()
best_model = pickle.load(open('best_model', 'rb'))
for key in companiescsv:
    titles = getData(key)
    new_positive_tweets = pd.Series(titles)
    df_counts_pos = tc.transform(new_positive_tweets)
    df_clean_pos = ct.transform(new_positive_tweets)
    df_model_pos = df_counts_pos
    df_model_pos['clean_text'] = df_clean_pos
    pred= best_model.predict(df_model_pos).tolist()
    positive = 0
    negative = 0
    neutral = 0
    for i in pred:
        if i == "negative":
            negative +=1
        if i == "neutral":
            neutral +=1
        if i == "positive":
            positive +=1
    print(key, negative, neutral, positive)
for key in companiescsvc:
    titles = getData(key)
    new_positive_tweets = pd.Series(titles)
    df_counts_pos = tc.transform(new_positive_tweets)
    df_clean_pos = ct.transform(new_positive_tweets)
    df_model_pos = df_counts_pos
    df_model_pos['clean_text'] = df_clean_pos
    pred= best_model.predict(df_model_pos).tolist()
    positive = 0
    negative = 0
    neutral = 0
    for i in pred:
        if i == "negative":
            negative +=1
        if i == "neutral":
            neutral +=1
        if i == "positive":
            positive +=1
    print(key, negative, neutral, positive)