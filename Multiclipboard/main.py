import sys 
import clipboard
import json


# create a function that can save data from the clipbaord to a json file
# make the function a write function , so that if the file does not exist the function will create it
def save_data(filepath , data ):
    with open(filepath, "w") as file :
        json.dump(data , file)

# create a function that can load data from a json file
def load_data(filepath):
    with open(filepath,"r")  as file:
        return json.load(file)



# following commands let you save , update , load data from the clipboard 
if len(sys.argv )==2:
    command = sys.argv[1]
    if command =="save":
        print("Save")
    if command == "load":
        print("Load")
    else:
        print("Command not found")

