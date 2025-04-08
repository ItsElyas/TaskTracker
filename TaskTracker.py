import json
import os
import datetime

USER_DATA = "UserData.json"

tasks = []
taskTracker = {}

def loadTasks():
    global taskTracker
    if os.path.exists(USER_DATA):
       with open(USER_DATA, "r") as jsonData:
           taskTracker = json.load(jsonData)
    
def saveTask(task):
    tasks.append(task)
    
def saveDict(tasks):
    today = datetime.datetime.today()
    today =today.strftime("%x")
    taskTracker.update({f"{today}: ": tasks})
    
    if today in taskTracker:
        taskTracker[today].update({f"{taskTracker}: ": tasks})

    with open(USER_DATA, "w") as jsonFile:
        json.dump(taskTracker, jsonFile, indent=4)
    
def printTasks():
    i = 1
    print("-------Tasks-------")
    for task in tasks:
        print(i,'.', task)
        i += 1

while True:
    userTask = input("Enter a task: ") 
    if userTask == 'q' or userTask == 'quit':
        json.dumps(taskTracker)
        break   
    saveTask(userTask)
    saveDict(tasks)
    
printTasks() # this prints the tasks
