#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import pandas as pd
import re
import sklearn


# In[2]:


from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# In[3]:


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
corpus = []


# In[4]:


dataset = pd.read_csv('SMSSpamCollection',sep='\t',names=["label","message"])


# In[5]:


# Data Preprocessing & Cleaning the text

for i in range(0,len(dataset)):
    review = re.sub('[^a-zA-Z]',' ',dataset["message"][i])
    review = review.lower()
    review = review.split()
#     review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words('english'))] 
    review = [stemmer.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    


# In[6]:


# Creating the Bag of words Model

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2500)


# Creating the TF-IDF Model

# from sklearn.feature_extraction.text import TfidfVectorizer
# cv = TfidfVectorizer(max_features=2500)

X = cv.fit_transform(corpus).toarray()


# In[7]:


y = pd.get_dummies(dataset['label'])
y = y.iloc[:,1].values


# In[8]:


# Train-Test Split (80:20)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=0)


# In[9]:


# Training model using Naive bayes classifier MultinomialNB

from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train, y_train)

y_pred=spam_detect_model.predict(X_test)


# In[10]:


# Confusion Matrix

from sklearn.metrics import confusion_matrix
confusion_m = confusion_matrix(y_test,y_pred)


# In[11]:


# Accuracy Score

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

