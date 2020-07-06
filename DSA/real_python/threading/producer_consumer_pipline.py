"""
message queue
queue system
data pip lines
thread safe consumer pip lines
"""

import random
import threading
import time
import concurrent.futures

FINISH = 'THE END'


class PipeLine:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None

    def set_message(self, msg):
        print(f'producing message of {msg}')
        producer_pipeline.append(msg)
        self.message = msg

    def get_message(self):
        print(f'consuming message of {self.message}')
        producer_pipeline.append(self.message)
        return self.message


def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)
    pipeline.set_message(FINISH)


def consumer(pipeline):
    message = None
    while message is not FINISH:
        message = pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())


producer_pipeline = []
consumer_pipeline = []
if __name__ == '__main__':
    pipeline = PipeLine(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exe:
        exe.submit(producer, pipeline)
        exe.submit(consumer, pipeline)
    print(f'producer {producer_pipeline}')
    print(f'consumer {consumer_pipeline}')
