import datetime
import time


#get the target time from the current time
def getGoalTime(user):
	DT=datetime.datetime.now()
	mMonth=DT.month*30*24*60
	mDay=DT.day*24*60
	mHour=DT.hour*60
	mMinute=DT.minute
	goalTime=mMonth+mDay+mHour+mMinute+user
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
	timeStamp.write(str(time2Stamp))
	timeStamp.close()

def tMer(remainingTime):
	tUp=False
	while(tUp==False):
		time.sleep(remainingTime)
		tUp=True
	
#this function is for the case when the computer is on for the time duration
#return how much time it has elapsed
def scScanNorm(user):
	gTime=getGoalTime(user)
	rTime=getReTime(gTime)
	timeStamp(rTime)
	tMer(rTime)
	#perform the scanning
	scScanNorm(user)

#cases when machine is off or crashed
#ran everytime when app is turned back on
rTime=0;
def scScanInt():
	with open("timeLog.txt","r") as t:
		rTime=t.read()
		t.close()
	#hit the exact 24 hour mark
	if (rTime==0):
		#perform scan
		print("Check 1")
	#It is over 24 hours mark, ask user if scanning should be performed
	elif rTime<0:
		#GUI asking for decisions
		print("Check 2")
	#count the remaining time
	#perform the scanning
	elif rTime>0:
		tMer(rTime)
		#perform the scanning
