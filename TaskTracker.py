import json
import os
import datetime

USER_DATA = "UserData.json"

tasks = []
taskTracker = {}

def loadTasks():
    if os.path.exists(USER_DATA):
        print("hello")
    
def saveTask(task):
    tasks.append(task)
    
def saveDict(tasks):
    taskTracker.update({f"{time.strftime("%x")}: ": tasks})
    
def printTasks():
    i = 1
    for task in tasks:
        print(i,'. ', task)
        i += 1


while True:
    userTask = input("Enter a task: ") 
    if userTask == 'q' or userTask == 'quit':
        break   
    saveTask(userTask)
    time = datetime.datetime.today()
    saveDict(tasks)
    
printTasks() # this prints the tasks
print(taskTracker)