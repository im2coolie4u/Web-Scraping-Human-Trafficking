#!/usr/bin/env python
# coding: utf-8


# Testing protoype or final code
#!/usr/bin/env python
# coding: utf-8


import requests
from requests import get
import urllib.request
import time
from bs4 import BeautifulSoup, NavigableString, Tag
import codecs
import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
stopword = nltk.corpus.stopwords.words('english')
from flair.models import TextClassifier
from flair.data import Sentence
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from urllib.request import urlopen
#from tkinter import *

def main():
	print("Please enter a URL: ")   #Enter any website, include the "https://" before you enter
	url1 = input()
	print("The website entered: ", url1)
	page1 = requests.get(url1)
	soup = BeautifulSoup(page1.text, 'html.parser')
	response1 = urllib.request.urlopen(url1)
	webContent = response1.read()

	#File1 is the html data of the website entered (.html file)
	#It is saved in the current directory and can be opened
	file1 = open('webpage_data.html', 'wb')
	file1.write(webContent)
	file1.close()

	#File2 is a text file containing all of the text from the webite entered
	#This file is also saved in the current directory and can be opened (.txt file)
	text_from_website = soup.get_text()
	file2 = open('webpage_data.txt', 'w+')
	file2.write(text_from_website)
	file2.close()

	#File4 is a text file that contains every single word and also 
	#phrases or also known as n-grams up to 4 words
	results = soup.find(id='ResultsContainer')
	file4 = open('lineByline.txt', 'w+')
	k = 0
	




	with open('webpage_data.txt', 'r') as file3:
		flat_list1=[words for line in file3 for words in line.split(" ")]#for line in file3:
	for words1 in flat_list1:
		file4.write(words1)
	term_matcher = 0


	soup.findAll('div')
	#url to sampled website: https://www.dhs.gov/blue-campaign/what-human-trafficking
	f = codecs.open("webpage_data.html", 'r')
	text = f.read()
	soup = BeautifulSoup(text, features="lxml")
	list(soup.children)
	paragraphs = soup.find_all('p')
	#paragraphs = soup.br.next_sibling
	#print(paragraphs)
	list1 = []
	for x in paragraphs:
		list1.append(str(x))

	separator = [','.join(ele.split()) for ele in list1]
	remove_bracket = str(list1)[1:-1]
	newset = remove_bracket



	words = newset.split()
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in words]
	#print(stripped)

	multigram_vector = CountVectorizer(ngram_range=(4,4), analyzer="word") #ngram range can be changed however needed
	X_counts = multigram_vector.fit_transform(list1)
	featurenames = multigram_vector.get_feature_names()
	multi_vector1 = multigram_vector.get_feature_names()
	multi_vector2 = np.asarray(multi_vector1)
	length_of_multi = len(multi_vector2)
	#print(multi_vector1)

		#term-frequency inverse document frequency
		#uses relative frequency to gather "important" words

	tfidf_vectorizer = TfidfVectorizer(analyzer="word")
	X_tfidf = tfidf_vectorizer.fit_transform(list1)
	print("\n")
	#print("Tfidf Vectorizer")




	single_vector1 = tfidf_vectorizer.get_feature_names()
	single_vector2 = np.asarray(single_vector1)
	length_of_single = len(single_vector2)
	#print("lenght of single_vector2 ", length_of_single)



			#Sentiment Analysis with Flair Library, Default model used, Pytorch Framework
	classifier = TextClassifier.load('en-sentiment')
	string_text = Sentence(newset)
	classifier.predict(string_text)
	print('Text Sentiment is: ', string_text.labels)
	sns.set(rc={'figure.figsize': (1000, 20)})
	sns.set_style("darkgrid")
	plt.title("Frequency Analysis of Words")
	frequency_words = nltk.FreqDist(stripped)
	frequency_words.plot(50)
	#plt.savefig("wprd_gra.png")
			

			#Count Vectorizer
	count_vect = CountVectorizer(analyzer="word")
	X_count = count_vect.fit_transform(list1)
	print("\n")
    

	y = 0
	while y < length_of_single:
		file4.write(single_vector2[y])
		file4.write("\n")
		y += 1

	z = 0
	while z < length_of_multi:
		file4.write(multi_vector2[z])
		file4.write("\n")
		z += 1

	file4.close()

	matched_terms = []

	file10 = open('lineByline.txt', 'r')
	file11 = open('traffick.txt', 'r')
	webpage_terms = file10.readlines()
	comparing_terms = file11.readlines()
	for line_webpage in webpage_terms:
		for line_compare in comparing_terms:
			if line_webpage == line_compare:
				term_matcher += 1
				matched_terms.append(line_compare)
			else:
				continue



	#length_of_X_tfidf = X_tfidf.shape[1]
	#print("Lenght of whafjasd ", length_of_X_tfidf)

	print("\n\n")
	print("Number of single words collected: ", length_of_single)
	print("Number of multi-word phrases collected: ", length_of_multi)
	print("This is how many terms matched: ", term_matcher)
	print("\n\n")

	if term_matcher >= 50:
		print("This website is extremely suspicious. Please leave the website immediately.")
	elif term_matcher < 50 and term_matcher > 5:
		print("This website is not safe. Proceed with caution.")
	else:
		print("This website is safe. Still proceed with caution.")

	print("\nThe terms that matched with the website: ")
	f = 0
	while f<len(matched_terms):
		print(matched_terms[f])
		f +=1 


main()
# Create a scoring method, maybe give a score between a 0-5
#We have good webistes and bad websites, what about neutral websites?
#Neutral sites area a grey area. Expand on this later

