from TVSeries import *
from movieScrap import *
from RecommendMovie import *
from deleteTables import *
while True:
	print("Enter you choice:")
	print("1. TV Series")
	print("2. Movie")
	n=int(input())
	if (n==1):
		print("Enter you choice:")
		print("1. Register new User")
		print("2. Mail current Users")
		print("3. Update Status of TV Series")
		print("4. View Registered Users")
		print("5. View Status of All registered series")
		print("6. Remove all registered users")
		i=int(input())
		if(i==1):
			registerUser()
		elif (i==2):
			mailUsers()
		elif(i==3):
			updateStatus()
		elif(i==4):
			viewRegisteredUser()
		elif(i==5):
			viewSeriesStatus()
		elif(i==6):
			delInfo()
		else:
			print("Invalid Choice")
	elif (n==2):
		print("1. Update Movie data")
		print("2. Email Recommend Movie")
		i=int(input())
		if(i==1):
			scrapData()
		elif (i==2):
			recommendMovie()
		else:
			print("Invalid Choice")
	else:
		print("Invalid Choice")
	check=input("Enter yes if you want to repeat these operation")
	if (check=="yes"):
		continue
	else:
		break
