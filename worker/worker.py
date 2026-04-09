import zmq
import time
import threading
import random

context = zmq.Context()

def worker_thread(id):
    socket = context.socket(zmq.REP)
    socket.connect("tcp://broker:5556")

    while True:
        msg = socket.recv_string()
        print(f"[Worker {id}] {msg}")

        time.sleep(random.uniform(0.5, 2))

        socket.send_string(f"OK {msg}")


if __name__ == "__main__":
    threads = []

    for i in range(3):
        t = threading.Thread(target=worker_thread, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
