# from containers import  Configs, Agents, Environments
from environments.environment import Environment
from environments.task_queue  import TaskQueue, Task
from environments.worker_pool import WorkerPool, Worker
from agents.random_agents     import RandomAgent
from agents.td_agents         import *

import time
import random

if __name__ == "__main__":

    # Configs.config.override({
    #     # TODO
    # })

    # Creamos una cola donde ir encolando las tareas
    myTaskQueue = TaskQueue()
    # Creamos el Pool con un tope de 10 workers
    myWorkerPool = WorkerPool(10)

    # Inicializamos el Pool con 5 workers
    for i in range(0,5):
        wrk = Worker()
        myWorkerPool.add_worker(wrk)
        
    myEnvironment = Environment(myWorkerPool, myTaskQueue)

    agent = RandomAgent()

    # Inicializamos state, reward y done
    state   = [myWorkerPool.get_num_workers(), 0, 0]
    reward  = 0
    done    = False

    try:
        past_num_tasks = 0
        while True:

            # Creamos una tarea cada cierto tiempo
            num = random.randint(1, 100)
            if num % 10 == 0:
                task = Task("Fichero")
                myEnvironment.task_queue.add_task(task)

            # Si tareas en la cola hay algun worker libre 
            # le asignamos la primera tarea pendiente 
            for wrk in myEnvironment.worker_pool.pool:
                if not wrk.is_running():
                    if myEnvironment.task_queue.get_num_tasks() > 0:
                        wrk.run_task(myEnvironment.task_queue.take_task())

            # El agente decide la siguiente accion y recoge 
            # el nuevo estado y la recompensa
            action = agent.act(state, reward, done)
            reward, state, done = myEnvironment.step(action, past_num_tasks)
            print("reward = {}, state= {}, done = {}".format(reward, state, done))        

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass

