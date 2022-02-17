#!/bin/bash

docker run -it --rm --network edge --name mosquitto_py_client -v $(pwd):/usr/src/myapp -w /usr/src/myapp python:3.11-rc-alpine sh -c 'pip install paho.mqtt && python mosquitto_client.py'
