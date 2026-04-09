import zmq
import threading
import time

context = zmq.Context()

frontend = context.socket(zmq.ROUTER)
frontend.bind("tcp://*:5555")

backend = context.socket(zmq.DEALER)
backend.bind("tcp://*:5556")

monitor_pub = context.socket(zmq.PUB)
monitor_pub.bind("tcp://*:5557")


def proxy():
    zmq.proxy(frontend, backend)


def monitor():
    while True:
        monitor_pub.send_string("STATUS Broker online")
        time.sleep(2)


if __name__ == "__main__":
    threading.Thread(target=monitor, daemon=True).start()
    proxy()
