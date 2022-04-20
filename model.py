import requests

class Task():
    def __init__(self, resourceReq1, resourceReq2, priority,filename):
        self.resourceReq1 = resourceReq1
        self.resourceReq2 = resourceReq2
        self.priority= priority 
        self.filename= filename


class Node():
    def __init__(self, ip, resourceAvail1, resourceAval2, isCloud):
        self.ip=ip
        self.resourceAvail1= resourceAvail1
        self.resourceAvail2 = resourceAval2
        self.isCloud = isCloud

        
    tasks={"task1":"complete", "task2":"running","task3":"waiting"}

    def checkIfResourceAvail(self, res1, res2):
        if(self.resourceAvail1>=res1 and self.resourceAvail2>=res2):
            return True
        return False
    
    def addTaskInWaiting():
        pass
    def markTaskCompleted(self,name):
        self.tasks[name]="Completed"
        return
    def markTaskAsRunning(self, name):
        self.tasks[name]="running"
        return
    def sendFileToclient(self,task):
        # http.    
        # task.filename send
        response=""
        with open("file_to_upload.txt", "rb") as a_file:
            file_dict = {task.filename: a_file}
            response = requests.post(f"http://{self.ip}:5000/runTask", files=file_dict,timeout= 120)
        print(response)
        print("task complete")
        return
    
    