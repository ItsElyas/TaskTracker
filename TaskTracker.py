import json
import os
import datetime

USER_DATA = "UserData.json"

tasks = []
taskTracker = {}

def loadTasks():
    global taskTracker
    global tasks
    if os.path.exists(USER_DATA):
       with open(USER_DATA, "r") as jsonData:
           taskTracker = json.loads(jsonData.read())
           today = getTime()
           tasks = taskTracker[f"{today}: "]
    
def saveTask(task):
    tasks.append(task)
    
def saveDict(tasks):
    today = getTime()
    taskTracker.update({f"{today}: ": tasks})
    
    if today in taskTracker:
        taskTracker[today].update({f"{today}: ": tasks})

    with open(USER_DATA, "w") as jsonFile:
        json.dump(taskTracker, jsonFile, indent=4)
        
def getTime():
    today = datetime.datetime.today()
    today =today.strftime("%x")
    return today
    
def printTasks():
    i = 1
    print("-------Tasks-------")
    for task in tasks:
        print(i,'.', task)
        i += 1

def printOptions():
    print("Welcome User!")
    print("1. Add Tasks")
    print("2. View Tasks")
    
printOptions()    
userInput = input()
      
loadTasks()


match userInput:
    
    case '1':
        while True:
            userTask = input("Enter a task: ") 
            if userTask == 'q' or userTask == 'quit':
                json.dumps(taskTracker)
                break   
            saveTask(userTask)
            saveDict(tasks)
    case '2':
        printTasks()
        
        
    
# printTasks() # this prints the tasks