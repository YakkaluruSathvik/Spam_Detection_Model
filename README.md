# Spam Detection Model Using Natural Language Processing(NLP)

## Analysis of Accuracy:

* Using _All features_ in creating model:

  1. Accuracy = 0.979372197309417 :: Using Stemming and Bag of Words Model
  2. Accuracy = 0.976681614349775 :: Using Lemmatization and Bag of Words Model

  3. Accuracy = 0.969506726457399 :: Using Stemming and TF-IDF Model
  4. Accuracy = 0.972197309417040 :: Using Lemmatization and TF-IDF Model

* For _max_features = 5000_ (top most frequent) in creating model:

  1. Accuracy = 0.984753363228699 :: Using Stemming and Bag of Words Model
  2. Accuracy = 0.982062780269058 :: Using Lemmatization and Bag of Words Model

  3. Accuracy = 0.973991031390134 :: Using Stemming and TF-IDF Model
  4. Accuracy = 0.976681614349775 :: Using Lemmatization and TF-IDF Model

* For _max_features = 2500_ (top most frequent) in creating model:

  1. Accuracy = __0.985650224215246__ :: Using Stemming and Bag of Words Model 
  2. Accuracy = 0.982959641255605 :: Using Lemmatization and Bag of Words Model 

  3. Accuracy = 0.979372197309417 :: Using Stemming and TF-IDF Model
  4. Accuracy = 0.979372197309417 :: Using Lemmatization and TF-IDF Model


## Summary:

##### 1. We will achieve maximum accuracy if we train our model with top maximum frequent accuring features(here features are words) rather than training with all features which decreases the accuracy of our model as we are considering less frequent features.

##### 2. One other reason for getting less accuracy is may be due to unequal number of data for spam & ham in dataset.

##### 3. Lemmatization takes more time than stemming but more precise than stemming.

##### 4. Here Stemming is preferred because meaning of the word is not important.

##### 5. TF-IDF Model is used when we need preference/importance for some words over other (like adjectives, adverbs).

##### 6. So, Our model is achieving an accuracy of 98.565% which is fair accuracy. [CountVectorizer and Stemming for top most 2500 features]
