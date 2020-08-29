import collections
import time
import random

class Task():
    
    def __init__(self, file):
        self.file = file
    
    def run(self):
        time.sleep(random.random()*100)


class TaskQueue():
    
    def __init__(self):
        self.number_of_tasks = 0
        self.queue           = collections.deque([]) 
        
    def add_task(self, task):
        self.number_of_tasks += 1
        self.queue.append(task)
        
    def take_task(self):
        if len(self.queue) > 0:
            self.number_of_tasks -= 1
            return self.queue.popleft()
        
    def get_num_tasks(self):
        return self.number_of_tasks