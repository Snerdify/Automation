import sys 
import clipboard
import json





if len(sys.argv )==2:
    command = sys.argv[1]
    if command =="save":
        print("Save")
    if command == "load":
        print("Load")
    else:
        print("Command not found")

