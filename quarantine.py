import os

file_list = []
root_directory = os.path.abspath(os.sep)
for sub_directories, directories, files in os.walk(root_directory):
    for my_file in files:
        filepath = sub_directories + os.sep + my_file
        # Should Check for virus behavior here first 
        # Waiting on that implementation 
        if filepath.endswith(".exe") or filepath.endswith(".dll"):
            file_list.append(my_file)

# Now create a quaranteened folder 
directory = os.path.dirname("/Quarantened_Files") 
if not os.path.exists(directory):
    os.makedirs(directory)
    
for each_file in files:
  old_location = os.path.dirname(os.path.abspath(each_file))
  new_location = directory + each_file
  os.rename(old_location,new_location)




