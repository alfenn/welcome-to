# https://docs.python.org/3/howto/sockets.html
import sys, json, socket
from typing import List
from threading import Thread, Lock


sys.path.append('../../../')
from my_python.players_adaptors_translators import NetworkPlayer, play_game
from my_python.PlayerState import PlayerState
from my_python.players_adaptors_translators import PlayerInterface
from my_python.calc_score import calc_score

##################################################################################################
##################################################################################################
### CONFIGURATION
##################################################################################################
##################################################################################################

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
# print(f'NUM_PLAYERS IS: {NUM_PLAYERS}', file=sys.stderr)



##################################################################################################
##################################################################################################
### 1. Set up play_game in its own thread
###     a. Each game's metadata and final playerstate is stored in all_players
### 2. Run the threads
##################################################################################################
##################################################################################################
# Threading setup:
#   - https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
#   - https://stackoverflow.com/questions/46301933/how-to-wait-till-all-threads-finish-their-work
threads: List[Thread] = [None] * NUM_PLAYERS
all_players: list = [None] * NUM_PLAYERS        # a list [[PlayerInterface, PlayerState], ...] storing the final state of each player
results: List[list] = []                        # a list following a8's ~myresults non-terminal [[ string, result:integer|false ], ...]
lock: Lock = Lock()

# Create each thread
for thread_player_id in range(NUM_PLAYERS):
    conn, addr = s.accept()
    # raise ValueError(f"Got connection to {conn}, {addr} successfully!")
    p = NetworkPlayer(conn)
    threads[thread_player_id] = Thread(target=play_game,
                                       args=(p, all_players, thread_player_id, lock))

# Start the threads
for t in threads:
    t.start()

# Stop the threads
for t in threads:
    t.join()        # Block the main execution thread until all created threads have finished executing: https://stackoverflow.com/questions/11968689/python-multithreading-wait-till-all-threads-finished

# print("All threads have finished running!", file=sys.stderr)
# for i in range(NUM_PLAYERS):
#     print(f'all_players[{i}] is not (None, None): {all_players[i][0] is not None and all_players[i][1] is not None}', file=sys.stderr)

##################################################################################################
##################################################################################################
### 3. Generate the result from each player
### 4. Append the result to results
##################################################################################################
##################################################################################################

for thread_player_id in range(NUM_PLAYERS):
    curr_player_interface: PlayerInterface = all_players[thread_player_id][0]
    curr_player_playerstate: PlayerState = all_players[thread_player_id][1]
    # Construct a list of temp values from all players besides the current player
    # Player's result will be "false" if they cheated, and their score otherwise
    player_result = None
    if curr_player_interface.marked_as_cheater:
        player_result = False
    else:
        all_other_temps = [all_players[i][1].temps for i in range(len(all_players)) if (i != thread_player_id
                                                                                        and not all_players[i][0].marked_as_cheater)]
        player_result = calc_score(curr_player_playerstate, all_other_temps)
    results.append([curr_player_interface.name, player_result])


##################################################################################################
##################################################################################################
### 5. Send scores to non-cheating players
### 6. Terminate connection with the players we just sent the scores to
##################################################################################################
##################################################################################################
for thread_player_id in range(NUM_PLAYERS):
    curr_player_interface: PlayerInterface = all_players[thread_player_id][0]
    if not curr_player_interface.marked_as_cheater:
        # Send the "game-over" a6 ~request non-terminal
        curr_player_interface.receive(json.dumps({"game-over": results}))
        resp = json.loads(curr_player_interface.send())
        if resp == "ack":
            curr_player_interface.terminate()

print(json.dumps(results))
# print(json.dumps(results), file=sys.stderr)
s.close()
