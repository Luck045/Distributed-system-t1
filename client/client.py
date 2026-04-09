import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://broker:5555")

for i in range(10):
    msg = f"Tarefa {i}"
    print(f"Enviando: {msg}")

    socket.send_string(msg)
    reply = socket.recv_string()

    print(f"Resposta: {reply}")
    time.sleep(1)
