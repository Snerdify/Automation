# multiclipboard 

import sys 
import clipboard
import json


# all of the data in the clipboard will be in json format 


# below is the code that will save the data in json and create a new json file with the passed
# in data  - write the data 
def save_items(filepath , data):
    with open(filepath ,"w") as file:
        json.dump(data , file)
#save_items("test.json" , {"key":"value"})

# below function will load the data from json - read the data
def load_items(filepath):
    with open(filepath ,"r" ) as file :
        return json.load(file)
load_items("test.json")



# these are the commands that will be used to save the data to the clipboard , load
# already saved data or change the data in the clipboard
if len(sys.argv) ==2:
    command = sys.argv[1]

    if command =="save":
        print("Save")
    elif command =="load":
        print("Load")
    else:
        print("Command not found")






