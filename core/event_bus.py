from queue import Queue
import threading

class EventBus:
    def __init__(self):
        self.queue = Queue()
        self.subscribers = []

    def publish(self, event):
        self.queue.put(event)

    def subscribe(self, handler):
        self.subscribers.append(handler)

    def start(self):
        def loop():
            while True:
                event = self.queue.get()
                for handler in self.subscribers:
                    handler(event)

        t = threading.Thread(target=loop)
        t.daemon = True
        t.start()
