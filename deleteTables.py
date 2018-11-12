import mysql.connector
from mysql.connector import errorcode
import config as c
def delInfo():
	try:
		mydb = mysql.connector.connect(
		host=c.MysqlHost,
		user=c.MysqlUser,
		passwd=c.MysqlPassword,
		database="mydatabase"
		) 
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		else:
			print(err)
	try:  
		mycursor = mydb.cursor()
		mycursor.execute("drop TABLE series_details")
	except:
		print("No table series_details")
	try:  
		mycursor = mydb.cursor()
		mycursor.execute("drop TABLE user_details")
	except:
		print("No table user_details")
	print("Deleted")

