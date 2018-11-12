import smtplib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from getDate import *
from datetime import date
import datetime
import mysql.connector
from mysql.connector import errorcode
import config
from mail import *
#Extracting Information about the series
def infoSeries(series):
	series=series.lower()
	series_name = series.split(" ")
	search_link = "https://www.imdb.com/find?ref_=nv_sr_fn&q="
	for word in range(len(series_name)):
		search_link += series_name[word]
		if word != len(series_name) - 1:
			search_link += "+"
	url=search_link+"&s=all"
	page = urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	l=list()
  
	for link in soup.findAll('a', href=True):
		if(" ".join(series_name) in str(link.string).lower()):
			l.append("https://www.imdb.com"+link['href'])
	quote_page = l[0]
	page = urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	name_box = soup.find('div', attrs={'class': 'seasons-and-year-nav'})
	a=name_box.find_all('a')
	done=1
	for x in a:
		season=x['href']
		final_link='https://www.imdb.com'+season
		#print(final_link)
		page = urlopen(final_link)
		soup = BeautifulSoup(page, 'html.parser')
		name_box = soup.find_all('span', attrs={'class': 'nobr'})
		name = name_box[0].text.strip()
		if name[-2]!=" " and name[-2]!="-":
			release_date= "The show has finished streaming all its episodes."
			done=0
		else:
			page = urlopen(final_link)
			soup = BeautifulSoup(page, 'html.parser')
			name_box = soup.find_all('div', attrs={'class': 'airdate'})
			l=0
			for item in name_box:
				name = item.text.strip() # strip() is used to remove starting and trailing
				ab=getNumberedDate(name)
				if len(name)!=0:
					if checkDate(int(ab))!=0 and len(name)==4:
						release_date="The next season begins in "+str(name)
						done=0
						break
					elif checkDate(ab)!=0:
						release_date="The next episode airs on "+str(checkDate(ab))
						done=0
						break
					else:
						l=1
						continue
				else:
					release_date="Information not available"
					done=1
					break
          
		if done==0:
			return release_date
		elif l==1:
			return "Information not available" 
		elif check==2:
			return "Information not available"
		elif done==1:
			continue
  

