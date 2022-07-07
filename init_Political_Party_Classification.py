#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json as js
import json_lines
import glob
import pandas as pd
import numpy as np 
import sklearn
import spacy
import seaborn as sns 
import re
import nltk
import wordcloud
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import string
from sklearn.naive_bayes import MultinomialNB
from pprint import pprint

print('ready')


# In[2]:


file = "data/ABaerbock.jl"


# In[3]:


def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text


# # Data Cleaning

# In[11]:


with json_lines.open(file) as jlf:
    for line in jlf:
        data = line['response']['data']
        for i in range(0, len(data)):
            # Remove all the special characters
            text = re.sub(r'\W', ' ', str(data[i]['text']))
            # remove all single characters
            text= re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
            # Remove single characters from the start
            text = re.sub(r'\^[a-zA-Z]\s+', ' ', text) 
            # Substituting multiple spaces with single space
            text = re.sub(r'\s+', ' ', text, flags=re.I)
            # Removing prefixed 'b'
            text = re.sub(r'^b\s+', '', text)
            # Converting to Lowercase
            text = re.sub('https://t.co','',text)
            text = re.sub('https','',text)
            text = re.sub(' co ','',text)
            text = re.sub('amp','',text)
            text = text.lower()
            text = remove_punct(text)
            data[i]['text'] = text
            print(data[56]['text'])
            #tweet cleaned
           
    #break
    
        


# In[5]:


with json_lines.open(file) as jlf:
    for line in jlf:
        data = line['response']['data']
        print(data[56]['text'])
        break


# # Vectorizing

# In[ ]:


processed_features = data.iloc[:,1].values
labels = data.iloc[:, 0].values
vectorizer = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8)
processed_features = vectorizer.fit_transform(processed_features).toarray()

