print ("=" * 10)


#This module allows you to ouput calendars. 
#It has built in functions to help. 
import calendar

def calendar_example ():
	#prints the day you have set to be the start of the week
	#in this case the default is 0 for Monday
	print (calendar.firstweekday())
	#prints what day of the week the date was on
	#0 = Monday, 1 = Tuesday, etc.
	print (calendar.weekday(2016, 8, 28))

calendar_example()


print ("=" * 10)


#This module identifies image file types.
import imghdr

def imghdr_example ():
	#Takes the image, considers the byte-stream, identifies type.
	print(imghdr.what('pizza2.jpg'))

imghdr_example()


print ("=" * 10)


#This module allows the manipulation of dates and times
import datetime

def datetime_example ():

	#fetches the current dates/times
	info = datetime.datetime.now()
	print("Year: {}".format(info.year))
	print("Month: {}".format(info.month))
	print("Day: {}".format(info.day))
	print("Hour: {}".format(info.hour))
	print("Minute: {}".format(info.minute))
	print("Second: {}".format(info.second))
	print("Microsecond: {}".format(info.microsecond))

datetime_example()


print ("=" * 10)
