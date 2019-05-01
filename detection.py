import pyclamd
import os
import sys
import re
import datetime
import time

def scanHis(result):
	cpath = os.getcwd()
	path = cpath + '/scanHistory/'

	path, dirs, files = next(os.walk(path))
	file_count = len(files)

	virusInfo=re.findall(r'\'(.*?)\'', result)
	virusNum=len(virusInfo)/3
	time=datetime.datetime.now()
	directory="Dir:"

	hist=open(path + "log%d.txt" %(file_count + 1), "w+")
	hist.write('Time:' + str(time)+'\n')
	hist.write(directory + '\n')
	hist.write('Virus:'+ '\n')
	i=0
	idx=0;
	while(idx<virusNum):
		hist.write('\t'+virusInfo[i] + ', ' + virusInfo[i+2] + '\n')
		idx=idx+1;
		i=i+3

	is_detected = 0
	if(virusNum == 0):
		hist.write('is_detected:' + str(is_detected) + '\n')
	else:
		is_detected=1
		hist.write('is_detected:' + str(is_detected) + '\n' )

	hist.close()


def init():
    engine = pyclamd.ClamdAgnostic()
    if (engine.ping()):
        print(engine.version())
        sys.stdout.flush()
        print(engine.reload())
        sys.stdout.flush()
        print(engine.stats())
        sys.stdout.flush()
    else:
        print('Connection failed (Not able to connect to Clamd)')
        sys.stdout.flush()

def scan_file(path):
    result = engine.scan_file(path)
    print('Detecting File: ' + path)
    sys.stdout.flush()
    if (result is None):
        print('No Virus Found In This File')
        sys.stdout.flush()
    else:
        print(result)
        sys.stdout.flush()


#This function is used for constantly scan a folder until finish
#print(engine.contscan_file('C:\\CFLog'))


if __name__ == '__main__':

    init()
    cpath = os.getcwd()
    path = cpath + '\\test'

    #Testing if single file detection works
    viruspath = path + '\\EICAR'
    noviruspath = path + '\\NO_EICAR'
    scan_file(viruspath)
    scan_file(noviruspath)

    #Testing if scan directory works
    print('Scanning Path: ' + path)
    sys.stdout.flush()
    print(engine.contscan_file(path))
