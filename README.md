Step 1: `docker network create -d overlay --attachable edge`

Step 2: Run `docker-compose up` in Terminal#1 to start mosquitto broker which is connected to that network 'edge'

Step 3: Run `run_subscriber.sh` in Terminal#2 to run an mqtt subscriber container which has subscribed to the topic 'python/mqtt'

Step 4: Run `run_python.sh` in Terminal#3 to run an mqtt publisher (the python script in this directory) which publishes to the topic 'python/mqtt'

Step 5: Observe Terminal#2 as it receives the messages sent by the python script in Terminal#3


