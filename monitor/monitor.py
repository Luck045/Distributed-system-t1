import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://broker:5557")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    msg = socket.recv_string()
    print(f"[Monitor] {msg}")
