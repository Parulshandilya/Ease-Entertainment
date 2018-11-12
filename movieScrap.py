import requests
from toCSV import *
from bs4 import BeautifulSoup
def scrapData(max_pages = 200):
	page = 0
	count = 0	
	fromYr=input("Enter start year: ")
	toYr=input("Enter end year: ")
	while page < max_pages:
		index = page * 50 + 1
		url =  'http://www.imdb.com/search/title?sort=year&start='+str(index)+'&title_type=feature&year='+fromYr+','+toYr
		page1=requests.get(url)
		soup=BeautifulSoup(page1.text,'html.parser')
		writeInTxtFile(soup)
		page+=1
def writeInTxtFile(soup):
	name_box = soup.find_all('div', attrs={'class': 'lister-item-content'})
	for item in name_box:
		try:
			title=item.find('h3',attrs={'class':'lister-item-header'})
			year=soup.find('span',attrs={'class':'lister-item-year text-muted unbold'})
			rating=soup.find('div',attrs={'class':'inline-block ratings-imdb-rating'})
			genre=soup.find('span',attrs={'class': 'genre'})
			genre_names=genre.getText().strip().split(',')
			if(year==None):
				year=" "
			else:
				year=year.getText()[1:-1]
			if(title==None):
				title=" "
			else:
				title=title.find('a').getText()
			if(rating==None):
				rating=" "
			else:
				rating=rating.getText().strip()
			for x in genre_names:
				f=open(str("data/"+x.strip())+'.txt','a')
				f.write(title + ',' + x + ',' + year + ',' + rating + '\n')
		except:
			print("ignored")

	toCSV()
