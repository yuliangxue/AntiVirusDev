import datetime
#import schedule

#get the target time from the current time
def getGoalTime(user):
	DT=datetime.datetime.now()
	mMonth=DT.month*30*24*60
	mDay=DT.day*24*60
	mHour=DT.hour*60
	mMinute=DT.minute
	goalTime=mMonth+ mDay+ mHour+mMinute+user
	return goalTime

#get the elapsed time, subtract currentTime from the goalTime
def getReTime(goalTime):
	DT=datetime.datetime.now()
	mMonth=DT.month*30*24*60
	mDay=DT.day*24*60
	mHour=DT.hour*60
	mMinute=DT.minute
	currT=mMonth+mDay+mHour+mMinute
	reTime=goalTime-currT
	timeStamp(reTime)
	return reTime

#update the remaining time into timeLog.txt
def timeStamp(time2Stamp):
	timeStamp=open("timeLog.txt","w+")
	timeStamp.write(time2Stamp)
	timeStamp.close()

#this function is for the case when the computer is off (intentionally or accidental)
#return how much time it has elapsed
def scScanNorm(user):
	gTime=getGoalTime(user)
	rTime=getReTime(gTime)
	#timer wait until rTime reaches 0 to execute
	#execute
	scScanNorm(user)

#cases when machine is off or crashed
#ran everytime when app is turned back on
def scScanInt(rTime):
	with open("timeLog.txt","r") as t:
		rTime=t.read()
		t.close()
	if (rTime==0):
		print("Check 1")
	elif rTime<0:
		print("Check 2")
	elif rTime>0:
		scScanNorm(user)
