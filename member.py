# -*- coding: utf-8 -*-

import timeouttimer

class Member:

    def __init__(self, address, heartbeat, client, t_cleanup):
        self.__address = address
        self.__heartbeat = heartbeat
        self.__timeouttimer = timeouttimer.TimeoutTimer(sleepTime=t_cleanup, client=client, member=self)

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

    def __eq__(self, other):
        return self.__address == other,__address

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self.__address[0]) + ":" + str(self.__address[1])

