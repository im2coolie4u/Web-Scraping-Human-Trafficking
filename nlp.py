from bs4 import BeautifulSoup
import codecs
import nltk
#import re
import string
#import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
stopword = nltk.corpus.stopwords.words('english')
from flair.models import TextClassifier
from flair.data import Sentence
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#from array import array

#url to sampled website: https://www.dhs.gov/blue-campaign/what-human-trafficking
f = codecs.open("index.html", 'r')
text = f.read()
#print(text)
soup = BeautifulSoup(text, features="lxml")
print(soup.prettify())
#print(soup.get_text())
list(soup.children)
print("\n")
#print(soup.title.text)
print("\n")
#body = soup.find('body')
#print(body)
# without_tags = body.findChildren(recursive=false)
#print(without_tags)
paragraphs = soup.find_all('li')
list = []
for x in paragraphs:
    list.append(str(x))
print(list)
print(type(list))
#remove_tags = soup.p.decompose
#print(remove_tags)
print("\n")
print(paragraphs)
print(type(paragraphs))
print("\n")
#table = soup.findAll('div',attrs={"class":"two-columns"})
#for x in table:
    #print(x.find('p').text)
    #print(x.find('a').text)

separator = [','.join(ele.split()) for ele in list]
remove_bracket = str(list)[1:-1]
newset = remove_bracket
print("\n")
print(newset)
print(type(newset))


#Debating whether this is worth doing or not since n-grams and tfidf vectorizer will contain stopwords...
#I take it back, I NEED THIS AFTER ALL
words = newset.split()
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print("\n")
print("Punctuations Begone")
print(stripped[:100])


#n-gram snippet
#vectorizes words and places words into a document matrix
multigram_vector = CountVectorizer(ngram_range=(4,4), analyzer="word") #ngram range can be changed however needed
X_counts = multigram_vector.fit_transform(list)
print("\n")
print("N-gram vectorizer/sampled:")
print(X_counts.shape)
print(multigram_vector.get_feature_names())
featurenames = multigram_vector.get_feature_names()
x_array = np.array(featurenames)
print("\n")
print(x_array)
print("\n")
print(x_array[10])

############################################3#
#def createMatrix(rowCount, colCount, dataList):
    #mat = []
    #for i in range(rowCount):
        #rowlist = []
        #for j in range(colCount):
            #rowlist.append(dataList[rowCount*i+j])
        #mat.append(rowlist)
    #return mat
#def main():
    #multigram_vector = CountVectorizer(ngram_range=(4, 4), analyzer="word")
    #X_counts = multigram_vector.fit_transform(list)
    #featurenames = multigram_vector.get_feature_names()
    #mat = createMatrix(10,10, featurenames)
    #print(mat)
    #print(mat[4])
    #print(type(mat))
#main()
#######################################################

#term-frequency inverse document frequency
#uses relative frequency to gather "important" words

tfidf_vectorizer = TfidfVectorizer(analyzer="word")
X_tfidf = tfidf_vectorizer.fit_transform(list)
print("\n")
print("Tfidf Vectorizer")
print(X_tfidf.shape)
print(type(x_array))
print(tfidf_vectorizer.get_feature_names())

#Sentiment Analysis with Flair Library, Default model used, Pytorch Framework
classifier = TextClassifier.load('en-sentiment')
string_text = Sentence(newset)
classifier.predict(string_text)
print("\n")
print('Text Sentiment is: ', string_text.labels)

#remove_string = newset.strip('"')
#print(remove_string)
#altered_set = remove_string.split()
#print(stripped)
#print(type(altered_set))
sns.set(rc={'figure.figsize': (1000, 20)})
sns.set_style("darkgrid")
plt.title("Frequency Analysis of Words")
frequency_words = nltk.FreqDist(stripped)
#frequency_words = nltk.FreqDist(altered_set)
frequency_words.plot(100)

#Count Vectorizer
count_vect = CountVectorizer(analyzer="word")
X_count = count_vect.fit_transform(list)
print("\n")
print(X_count)
print(count_vect.get_feature_names())
