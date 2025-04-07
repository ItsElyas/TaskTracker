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
    time = datetime.datetime.today()
    taskTracker.update({f"{time.strftime("%x")}: ": tasks})
    
    with open(USER_DATA, "w") as jsonFile:
        json.dump(taskTracker, jsonFile, indent=4)
    
def printTasks():
    i = 1
    print("-------Tasks-------")
    for task in tasks:
        print(i,'.', task)
        i += 1



userTask = input("1. Add Task\n2. Remove Task\n3. View Tasks\n4. View Daily task %\n")

while True:
    userTask = input("Enter a task: ") 
    if userTask == 'q' or userTask == 'quit':
        json.dumps(taskTracker)
        break   
    saveTask(userTask)
    saveDict(tasks)
    
printTasks() # this prints the tasks
print(taskTracker)