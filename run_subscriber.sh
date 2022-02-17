#!/bin/bash

docker run -it --rm --network edge alpine sh -c 'apk add mosquitto-clients && mosquitto_sub -h mosquitto -t python/mqtt'
