# -*- coding: utf-8 -*-

import socket

class Client:
#    __random
#    __server
#    __me

    def __init__(self):
        self.__memberList = []
        self.__deadList = []
        self.__t_gossip = 1000
        self.__t_cleanup = 10000
        self.__myAddress = socket.gethostbyname('localhost')

    def parseStartupMembers(self):
        pass

    def sendMembershipList(self):
        pass

    def getRandomMember(self):
        pass

    class MembershipGosspier:
        def __init__(self):
            pass

        def run(self):
            pass

    class AsynchronousReceiver:
        def __init__(self):
            pass

        def run(self):
            pass

        def mergeLists(self):
            pass

    def start(self):
        gossiper = self.MembershipGosspier()
        reciver = self.AsynchronousReceiver()

    def handleNotification(self):
        pass

if __name__ == '__main__':
    client = Client()
    client.start()
