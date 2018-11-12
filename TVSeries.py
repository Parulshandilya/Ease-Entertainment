from infoSeries import *
import mysql.connector
from mysql.connector import errorcode
import config
from mail import *
#Connecting with MySql
def databaseConnection():
	try:
		mydb = mysql.connector.connect(
			host=MysqlHost,
			user=MysqlUser,
			passwd=MysqlPassword,
			database="mydatabase"
		)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		else:
			print(err)
	mycursor = mydb.cursor()
	try:
		mycursor.execute("CREATE DATABASE mydatabase")
	except:
		pass
	try:
		mycursor.execute("CREATE TABLE user_details(Id INT AUTO_INCREMENT PRIMARY KEY,Email VARCHAR(255), series VARCHAR(255))")
	except:
		pass
	try:
		mycursor.execute("CREATE TABLE series_details(series VARCHAR(255),status VARCHAR(255))")
	except:
		pass
	return mydb
def registerUser():
	mydb=databaseConnection()
	mycursor = mydb.cursor()
	print("Enter Number of Users you want to Register")
	n=int(input())
	for i in range(n):
		x=input("\nEmail address:")
		tv=input("TV series:")
		sql="INSERT INTO user_details(Email,series) VALUES(%s, %s)" 
		val=(x,tv)
		mycursor.execute(sql,val)
		mydb.commit()
		for k in tv.split(','):
			xx=k.strip()
			mm=infoSeries(xx)
			sql="insert into series_details (series,status) values(%s,%s)" 
			val=(xx,mm)
			mycursor.execute(sql,val)
			mydb.commit()
def mailUsers():
	mydb=databaseConnection()
	mycursor = mydb.cursor()
	seriesDetail={}
	mycursor.execute("SELECT series,status FROM series_details")
	for x in mycursor:
		#print(x[0])
		if x[0] not in seriesDetail:
			seriesDetail[x[0]]=x[1]
	mycursor.execute("SELECT Email,series FROM user_details")
	for x in mycursor:
		message=''
		for k in x[1].split(','):
			xx=k.strip()	
			message+="Tv series name: "+str(xx)+"\r\n"+"Status: "+seriesDetail[xx]+"\r\n"    
			message+="\r\n"
		email(x[0],message,"TV series Status")
def updateStatus():
	mydb=databaseConnection()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT series FROM series_details")
	series=[]
	for x in mycursor:
		series.append(x[0])
	for i in series:
			mm=infoSeries(i)
			mycursor = mydb.cursor()
			mycursor.execute ("""UPDATE series_details SET status=%s WHERE series=%s""", (mm,i))
			mydb.commit()
def viewRegisteredUser():
	mydb=databaseConnection()
	mycursor=mydb.cursor()
	mycursor.execute("SELECT Email,series FROM user_details")
	for x in mycursor:
		print("Email: "+x[0])
		print("Series: "+x[1])
		print()	
def viewSeriesStatus():
	mydb=databaseConnection()
	mycursor=mydb.cursor()
	mycursor.execute("SELECT series,status FROM series_details")
	for x in mycursor:
		print("Series: "+x[0])
		print("Status: "+x[1])
		print()	
	
