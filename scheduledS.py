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
	goalT=open("goalT.txt","w+")
	goalT.write(str(goalTime))
	goalT.close()

	return goalTime

#get the elapsed time, subtract currentTime from the goalTime
def getReTime():
	with open("goalT.txt","r") as t:
		readGTime=t.read()
		t.close()

	DT=datetime.datetime.now()
	mMonth=DT.month*30*24*60
	mDay=DT.day*24*60
	mHour=DT.hour*60
	mMinute=DT.minute
	currT=mMonth+mDay+mHour+mMinute
	reTime=readGTime-currT
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
	tMer(rTime)
	#perform the scanning

#cases when machine is off or crashed
#ran everytime when app is turned back on
def scScanInt():
	with open("timeLog.txt","r") as t:
		rTime=t.read()
		t.close()
	if rTime==0:
		#perform scan
		print("Check 1")
	elif rTime<0:
		#perform the scanning
		print("Check 2")
	elif rTime>0:
		tMer(rTime)
		#perform the scanning
