import sys 
import clipboard
import json

# this is the json file in which the data will be saved 
DATA_JSON = "data.json"
# create a function that can save data from the clipbaord to a json file
# make the function a write function , so that if the file does not exist the function will create it
def save_data(filepath , data ):
    with open(filepath, "w") as file :
        json.dump(data , file)

# create a function that can load data from a json file
def load_data(filepath):
    try:
        with open(filepath,"r")  as file:
            return json.load(file)
    except:
        return {}



# following commands let you save , update , load data from the clipboard 
if len(sys.argv )==2:
    command = sys.argv[1]
    if command =="save":
        data = load_data(DATA_JSON)
#Save command should save the current clipboard content to a file as a value pair to 
# a key that is provided by the user
        key = input("Enter the key for the clipboard data:")
        data[key] = clipboard.paste()
        save_data(DATA_JSON , data)


        print("Data Saved")
    if command == "load":
        print("Load")
    else:
        print("Command not found")

