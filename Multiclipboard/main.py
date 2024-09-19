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
    data = load_data(DATA_JSON)
    if command =="save":
        
#Save command should save the current clipboard content to a file as a value pair to 
# a key that is provided by the user
        key = input("Enter the key for the clipboard data:")
        data[key] = clipboard.paste()
        save_data(DATA_JSON , data)
        print("Data Saved")
    elif command == "load":
        key = input("Enter the key for the clipboard data:")
        if key in data :
            clipboard.copy(data[key])
            print("Data copied from clipboard")
        else:
            print("Key not found")

    elif command == "list":
        print(data)
        
    else:
        print("Command not found")

