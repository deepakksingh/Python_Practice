"""
Usage:
    This code will create a cross product of parameters and start training(just a while loop here).
    The user can interrupt the program by using 'kill -<signal_number/signal_name> <process_id>'
    The code will be interrupted and the training will begin for the next combination of parameters.

    Here a single signal handler has been registered for all possible signals, but an extended case
    can have different handlers as per need.
"""

from itertools import product
from collections import OrderedDict
from collections import namedtuple
import time
import numpy as np
import signal
import os
import time

class RunBuilder():

    def __init__(self,params):
        self.runs = []
        self.current_run_index = 0
        self.current_run_params = None
        print(f"1")
        self.process_runs(params)
        


    def process_runs(self, params):
        print(f"2")
        Run = namedtuple('Run',params.keys())

        for v in product(*params.values()):
            self.runs.append(Run(*v))


    # @staticmethod
    def get_next_run(self):
        print(f"4")
        if self.current_run_index == len(self.runs):
            print(f"Out of run params")
            exit()

        else:
            self.current_run_params = self.runs[self.current_run_index]
            self.current_run_index += 1
            return self.current_run_params

def train_loop(run):
    print(f"run:{run}")
    global interrupted
    while True:
        print(f"My PID is: {os.getpid()}")
        print(f"run: {run}")
        print(f"Training loop...waiting for interrupts!")
        time.sleep(5)
        if interrupted:
            return


def receiveSignal(signal_number, frame):
    print(f"Received: {signal_number}")
    # print([k for k in np.arange(1000)])
    print(f"setting interrupted flag")
    global interrupted 
    interrupted = True
    return


interrupted = False

def main():

    params = OrderedDict(
        lr = [0.001,0.01,0.1],
        momentum = [0.9,0.85],
        batch_size = [8,16,24,32],
    )

    global interrupted

    run_builder_obj = RunBuilder(params)

    for i in range(len(run_builder_obj.runs)):
        #get a run obj
        print(f"3")
        run_obj = run_builder_obj.get_next_run()
        #train on run obj
        train_loop (run_obj)

        if interrupted:
            interrupted = False
            continue


if __name__ == "__main__":
    # register the signals to be caught
    signal.signal(signal.SIGHUP, receiveSignal)
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)
    main()