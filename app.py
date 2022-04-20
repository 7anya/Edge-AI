from flask import Flask, request
from werkzeug.utils import secure_filename
from model import *
from scheduler import *
app = Flask(__name__)
ips=[]



@app.route('/')
def hello_world():
    return '<h1>Hello from Docker</h2>\n'

@app.route('/ip', methods=["GET"])
def registerIp():
    ip = request.args.get('ip')
    ips.append(ip)
    return 200


@app.route('/dockerstat', methods=["POST"])
def acceptDockerStats():
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
    #   filename must pe ip.csv
    #   process stats
      return 'file dockerstats uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True, port=5000)