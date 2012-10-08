# -*- coding: utf-8 -*-

class Member:
    __address
    __heartbeat
    __timeouttimer

    def __init__(self, address, heartbeat, client, t_cleanup):
        self.__address = address
        self.__heartbeat = heartbeat
        self.__timeouttimer = TimeoutTimer(t_cleanup=t_cleanup, client=client, source=self)

    def startTimeoutTimer(self):
        self.__timeouttimer.start()

    def resetTimeoutTimer(self):
        self.__timeouttimer.reset()

    @property
    def address(self):
        return self.__address

    def getHeartbeat(self):
        return self.__heartbeat

    def setHeartbeat(self, heartbeat):
        self.__heartbeat = heartbeat

    heartbeat = property(getHeartbeat, setHeartbeat)

    def __eq__(self):
        pass()

    def __hash__(self):
        pass()

