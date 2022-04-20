from model import *
import threading

threads=[]
tasksToDo=[Task(1,2,"high","one.sh"),Task(2,3,"low","two.sh")]
tasksDone=[]

nodesOnEdge=[Node("17.9.0.8",1,2, False), Node("17.9.0.9",4,2, False)]
nodesOnCloud=[Node("17.9.0.8",1,2, True), Node("17.9.0.9",4,2, True)]

def scheduleTasksFFCS():
    while(len(tasksToDo)!=0):
        for task in tasksToDo:
            isScheduled= False
            for node in nodesOnEdge:
                if(node.checkIfResourceAvail(task.resourceReq1,task.resourceReq2)):
                    threaD=threading.Thread(target=node.sendFileToclient,args=(task.filename) )
                    threads.append(threaD)
                    threaD.start()                  
                    isScheduled=True
                    tasksToDo.pop(0)
            if isScheduled==False and task.priority=="high":
                for node in nodesOnCloud:
                    if(node.checkIfResourceAvail(task.resourceReq1,task.resourceReq2)):
                        threaD=threading.Thread(target=node.sendFileToclient,args=(task.filename) )
                        threads.append(threaD)
                        threaD.start()
                        isScheduled=True
                        tasksToDo.pop(0)
        for index, thread in enumerate(threads):
            thread.join()
    





            




        