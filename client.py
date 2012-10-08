# -*- coding: utf-8 -*-

import socket

class Client:
    __memberList = []
    __deadList = []
    __t_gossip
    __t_cleanup
    __random
    __server
    __myAddress
    __me

    def __init__(self):
        __t_gossip = 1000
        __t_cleanup = 10000
        __myAddress = socket.gethostbyname('localhost')

    def parseStartupMembers(self):
        pass()

    def sendMembershipList(self):
        pass()

    def getRandomMember(self):
        pass()

    class MembershopGosspier:
        def __init__(self):
            pass()

        def run(self):
            pass()

    class AsynchronousReceiver:
        def __init__(self):
            pass()

        def run(self):
            pass()

        def mergeLists(self):
            pass()

    def start(self):
        pass()

    def handleNotification(self):
        pass()
