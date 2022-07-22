from threading import Thread, Lock
from time import sleep
from random import random
import json, socket, sys
sys.path.append('../../../')


### Read in network config from stdin
network_config = json.loads(sys.stdin.read())
### Set up the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = ('localhost', network_config["port"])
s.bind(ADDR)
NUM_PLAYERS = network_config["players"]
s.listen(NUM_PLAYERS)
### Print confirmation to stdout that server has been set up
print(json.dumps("started"))
sys.stdout.flush()

print(f"NUM_PLAYERS: {NUM_PLAYERS}",file=sys.stderr)


def target(i, lock, results):
    with lock:
        print("Starting thread {}".format(i), file=sys.stderr)
    # Do something
    r = random()*2
    sleep(r)
    with lock:
        results[i] = r
    with lock:
        print("Stopping thread {}".format(i), file=sys.stderr)

# Create the threads
lock = Lock()
mythreads = [None] * NUM_PLAYERS
myresults = [None] * NUM_PLAYERS
# threads = [Thread(target=target, args=(i, lock)) for i in range(5)]
for i in range(NUM_PLAYERS):
    conn, addr = s.accept()
    mythreads[i] = Thread(target=target, args=(i, lock, myresults))

# Start the threads
for x in mythreads:
    x.start()

# Stop the threads
for x in mythreads:
    x.join()

print("Done!", file=sys.stderr)
print(f"results: {myresults}", file=sys.stderr)
raise ValueError('8.1 testdriver1 done====')
