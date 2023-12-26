
import time
from uix.core.pipe import Pipe

class status_pipe(Pipe):
    def __init__(self):
        self.total_events = 0
        self.number_of_events = 0
        self.events_per_second = 0
        self.time_start = time.time()
        self.time_end = time.time()
    
    def calc_events_per_second(self):
        self.time_end = time.time()
        self.events_per_second = self.number_of_events / (self.time_end - self.time_start)
        self.time_start = time.time()
        self.total_events += self.number_of_events
        self.number_of_events = 0
        print("Events per second: " + str(self.events_per_second) + " Total events: " + str(self.total_events))

    def run(self, sid, data):
        self.number_of_events += 1
        if self.number_of_events > 10:
            self.calc_events_per_second()
        return data