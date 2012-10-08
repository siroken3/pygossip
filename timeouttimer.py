# -*- coding: utf-8 -*-

import threading

class TimeoutTimer:
    __sleepTime
    __client
    __timer
    __source

    def __init__(self, sleepTime, client, member):
        self.__sleepTime = sleepTime
        self.__client = client
        self.__timer = threading.Timer(self.sleepTime, self.__client.handleNotification)
        self.__source = member

    def start(self):
        self.reset()
        self.__timer.start()

    def reset(self):
        self.__timer = threading.Timer(sleepTime, client.handleNotification, kwargs={})
