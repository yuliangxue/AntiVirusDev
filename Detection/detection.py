import pyclamd
import os
import sys
import re

engine = pyclamd.ClamdAgnostic()

def init():
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

    print(viruspath)

    #Testing if scan directory works
    print('Scanning Path: ' + path)
    sys.stdout.flush()
    print(engine.contscan_file(path))
