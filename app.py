
import socket
from urllib import response
from flask import Flask, request
from werkzeug.utils import secure_filename
import os

import requests
app = Flask(__name__)
ip=""

def registerip():
    ip=socket.gethostbyname(socket.gethostname() )  
    response= requests.get("http://192.168.220.129:5000/ip",params={"ip":ip})
    print(response)
    return 

registerip() 

def sendDockerStats():

    stream= popen(f"chmod +x stats.sh && ./stats.sh")
    stat=stream.read()
    response= requests.post("http://192.168.220.129:5000/ip",data={"ip": ip, "stat":stat})
    return response
    
    

@app.route('/')
def hello_world():
    return '<h1>Hello from inside</h2>\n'

@app.route('/runTask',methods=["POST"])
def runTask():
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      stream= popen(f"chmod +x {f.filename} && ./{f.filename}")
      return stream.read()
    

if __name__ == "__main__":
    
    app.run(debug=True, port=5000)