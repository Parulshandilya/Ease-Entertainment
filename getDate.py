import datetime
#Converting Date format
def getNumberedDate(date):
	if len(date)==0:
		return 0
	datesDict = {'Jan.':1,'Feb.':2,'Mar.':3,'Apr.':4,'May':5,'Jun.':6,'Jul.':7,'Aug.':8,'Sep.':9,'Oct.':10,'Nov.':11,'Dec.':12}
	numberedDate = 1
	if(len(date) == 4):
		numberedDate = int(date)
		return numberedDate
	splits = date.split(" ")
	if len(splits)==3:
		date,month,year = splits
		month = datesDict[month]
	else:
		date=date[0:1]
		month=date[2:-4]
		year=date[-4:]
	numberedDate = int(year)
	numberedDate *= 100
	numberedDate += int(month)
	numberedDate *= 100
	numberedDate += int(date)
	return numberedDate
	
	
	
#Functions Used to Abstract Information about the TV series release date
def checkDate(ab):
	if(ab==0):
		return 0
	today=datetime.datetime.now()
	dd=today.day
	mm=today.month
	yyyy=today.year
	if len(str(ab))==4:
		if yyyy<=int(ab):
			return ab
	else:
		return 0
	d=int(ab%100)
	ab=ab/100
	m=int(ab%100)
	ab=ab/100
	y=int(ab)
	if yyyy<y:
		return datetime.date(y,m,d)
	elif yyyy==y:
		if mm<m:
			return datetime.date(y,m,d)
		elif mm==m:
			if dd<=d:
				return datetime.date(y,m,d)
			else:
				return 0
		else:
			return 0
	else:
		return 0 

