class Environment():
    
    def __init__(self, worker_pool, task_queue):
        self.worker_pool    = worker_pool
        self.task_queue     = task_queue
        self.avg_time       = 0
        
    
    def step(self, action, past_num_tasks):

        reward, done = 0, 0

        if action == 0:         # if action is 0, check status and give reward
            if self.task_queue.get_num_tasks() > past_num_tasks:
                reward -= .3        # reward of -0.3
            else:
                reward += .3
    
        if action == 1:         # if action is 1, add Worker to the Pool
            wrk = Worker()
            self.worker_pool.add_worker(wrk)
            reward -= .1        # reward of -0.1

        if action == 2:         # if action is 2, remove Worker from the Pool 
            self.worker_pool.remove_worker()
            reward += .1        # reward of -0.1


        # creating the state vector
        state = [self.worker_pool.get_num_workers(), 
                 self.task_queue.get_num_tasks(), 
                 self.avg_time]

        return reward, state, done
