import datetime

tasks = []
taskTracker = {}

def saveTask(task):
    tasks.append(task)
    
    
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
    taskTracker.update({f"{time.strftime("%x")}: ": tasks})
    
printTasks() # this prints the task
print(taskTracker)