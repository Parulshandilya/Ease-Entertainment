#%matplotlib inline
import sys,csv,operator
from  matplotlib import pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from mail import *
value_list=['Horror', 'Drama', 'Comedy', 'Action', 'Biography', 'Crime',
       'Thriller', 'Adventure', 'Family', 'Animation', 'Mystery', 'Sci-Fi',
       'Fantasy', 'Western', 'Romance', 'Music',  'War', 'Musical', 'History']

def recommendMovie():
	mail=input("Enter your email address: ")
	print ("Select the input: " + '\n '.join(value_list) + "\n")
	user_genre = input("What genre of movies do you like?")
	genre_names=user_genre.strip().split(',')
	genre=genre_names
	message=""
	for q in genre:
		message+="\r\n"
		#print ('According to your choice of gener and year we recomend theses movies'+q)
		data = pd.read_csv("data/txt/"+q+'.txt', sep=",", header = None,error_bad_lines=False)
		data.columns = ["movie_name", "genre", "year", "rating"]
		top_five =  data.sort('rating', ascending=False).head(5)
		l=top_five.values.T.tolist()
		print(top_five.movie_name)
		message+="Movies recommended for genre: "+q+"\r\n\r\n"
		for x in l[0]:
			message+=str(x)    
			message+="\r\n"
	email(mail,message.encode('ascii', 'ignore').decode('ascii'),"Recommended Movies")
