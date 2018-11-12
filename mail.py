import smtplib
from config import *
###user credential details block
#Email
EmailAddress=email
Password=password

#Mailing Function
def email(email,message,subject): 
	#Please add the email address by which you want to send the mail
	fromaddr = EmailAddress
	toaddrs  = email
	msg = "\r\n".join([
		"From: your_email_address",
		"To:"+toaddrs,
		"Subject: "+subject,
		"",
		message
		])
	username = fromaddr
	#Please add the password of your email address
	password = Password
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
	print("Mailed to "+email)
