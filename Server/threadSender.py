import pygame
import threading
import socket


class ThreadSender(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.counter = counter

    def run(self):
        pass

    def __start_listen(self):
        pass
