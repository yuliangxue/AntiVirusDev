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
        #Adding Functionality:
        # I am going to make this function return a Bool
        # This makes it easier to integrate with Quarantine
        return False
    else:
        print(result)
        sys.stdout.flush()
        # As mentioned above, adding this to save time 
        return True


#This function is used for constantly scan a folder until finish
#print(engine.contscan_file('C:\\CFLog'))

def multiscan():
    #
    #Multi-File Detection
    # print directory to see error
    # May need to use regular expression to replace all slash with double slash
    file_list = []
    root_directory = os.path.abspath(os.sep)
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    for sub_directories, directories, files in os.walk(desktop):
        for my_file in files:
            filepath = sub_directories + os.sep + my_file
            # Check for virus behavior here
            print("FILE TO SCAN:   " + filepath)
            if scan_file(my_file) == True:
                file_list.append(my_file)
    return file_list

def multiquarantine(file_list):
    #Multi-File Quarantine
    quarantine_directory = os.path.dirname("/Quarantened_Files") 
    if not os.path.exists(quarantine_directory):
        os.makedirs(quarantine_directory)
    
    for each_file in file_list:
      old_location = os.path.dirname(os.path.abspath(each_file))
      new_location = quarantine_directory + each_file
      os.rename(old_location,new_location)

def multideletion():
    #Multi-File Deletion
  
    for files in os.walk(quarantine_directory):
            user_input = input("Enter 1 to delete the following file:" + files)
            if(user_input == 1):
                os.remove(files)

    print()
    ### No longer needed
    user_response = input("Enter 2 to view all remaining files in Quarantined folder")
    if(user_response == "2"):
        for files in os.walk(quarantine_directory):
            print(files)
    ### No longer needed 
    
    
if __name__ == '__main__':

    init()
    cpath = os.getcwd()
    path = cpath + '\\Detection\\test'

    #Testing if single file detection works
    viruspath = path + '\\EICAR'
    noviruspath = path + '\\NO_EICAR'
    print(scan_file(viruspath))
    print(scan_file(noviruspath))

    #Testing if scan directory works
    print('Scanning Path: ' + path)
    sys.stdout.flush()
    quarantined_files = multiscan()
    multiquarantine(quarantined_files)
    multideletion()
    

    


    


    
