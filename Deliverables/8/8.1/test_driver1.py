import sys, json, socket, threading

network_config = json.loads(sys.stdin.read())
PORT = network_config["port"]
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    server.listen()
    while True:
        print(json.dumps('started'), flush=True)
        conn, addr = server.accept()

        raise ValueError('SERVER is startginggggg')
start()
