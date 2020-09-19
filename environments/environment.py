from environments.task_queue  import TaskQueue, Task
from environments.worker_pool import WorkerPool, Worker
from config import *
import numpy as np

class Environment():
    
    # def __init__(self):
    #     # Creamos el Pool con un tope de 10 workers
    #     self.worker_pool = WorkerPool(MAX_NUM_WORKERS)
    #     # Cola donde ir encolando las tareas        
    #     self.task_queue  = TaskQueue()
    
    def reset(self):
        # Creamos el Pool con un tope de 10 workers
        self.worker_pool = WorkerPool(MAX_NUM_WORKERS, INITIAL_WORKERS)
        # Cola donde ir encolando las tareas        
        self.task_queue  = TaskQueue() 
        return [self.worker_pool.get_num_workers(), 0, 0, 0] 
        
    
    def step(self, action, past_num_tasks):

        reward, done = 0, False

        if action == 0:         # if action is 0, do nothing, check status and give reward
            if self.task_queue.get_num_tasks() > past_num_tasks:
                reward += ACTION_0_UP_REWARD
            else:
                reward += ACTION_0_DOWN_REWARD
    
        if action == 1:         # if action is 1, add Worker to the Pool
            wrk = Worker()
            self.worker_pool.add_worker(wrk)
            reward += ACTION_1_REWARD        

        if action == 2:         # if action is 2, remove Worker from the Pool 
            self.worker_pool.remove_worker()
            reward += ACTION_2_REWARD      


        # Discretizamos el tiempo medio de estancia en la cola en varios niveles
        time_in_queue_category = np.digitize(self.task_queue.avg_time_in_queue, BINS, right=False)
        if time_in_queue_category == len(BINS):
            done = True

        # creating the state vector
        state = [self.worker_pool.get_num_workers(),
                 self.worker_pool.get_num_workers_running(),        
                 self.task_queue.get_num_tasks(), 
                 time_in_queue_category]

        return state, reward, done
