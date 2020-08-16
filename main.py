from containers import  Configs, Agents

import threading
import time
import random
import collections
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

if __name__ == "__main__":

    Configs.config.override({
        # TODO
    })

    agent = Agents.random_agent

    # Creamos una cola donde ir encolando las tareas
    myTaskQueue = TaskQueue()
    # Creamos el Pool con un tope de 10 workers
    myWorkerPool = WorkerPool(10)

    # Inicializamos el Pool con 5 workers
    for i in range(0,5):
        wrk = Worker()
        myWorkerPool.add_worker(wrk)
        
    myEnvironment = Environment(myWorkerPool, myTaskQueue)

    try:
        past_num_tasks = 0
        while True:
            # Creamos una tarea cada cierto tiempo
            num = random.randint(1, 10000)
            if num % 1000 == 0:
                task = Task("Fichero")
                myEnvironment.task_queue.add_task(task)
                
            for wrk in myEnvironment.worker_pool.pool:
                if not wrk.is_running():
                    if myEnvironment.task_queue.get_num_tasks() > 0:
                        wrk.run_task(myEnvironment.task_queue.take_task())

            #print("Number of Tasks   = {}".format(myEnvironment.task_queue.get_num_tasks()))
            #print("Number of Workers = {}".format(myEnvironment.worker_pool.get_num_workers()))
            
            # Comenzamos con un agente que seleccione las acciones al azar
            action = agent.act(state, reward, done)
            reward, state, done = myEnvironment.step(action, past_num_tasks)
            print("reward, state, done = {}, {}, {}".format(reward, state, done))        



    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass

