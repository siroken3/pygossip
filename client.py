# -*- coding: utf-8 -*-

import sys
import socket
import random
import pickle
import threading
import member
import time

class Client:
#    __random
#    __server

    def __init__(self, startupHostsList):
        self.__memberList = []
        self.__deadList = []
        self.__t_gossip = 1000
        self.__t_cleanup = 10000
        port = 0
        myIpAddress = socket.gethostbyname('localhost')
        self.__myAddress =  (myIpAddress, port)

        for host in startupHostsList:
            member = Member(host, 0, self, self.t_cleanup)
            if host.count(myIpAddress) > 0:
                self.__me = member
                port = host[1]
                self.__myAddress = (myIpAddress, port)
            self.__memberList.append(member)

        print "Original Member List"
        print "--------------------"
        for member in self.__memberList:
            print member

        if port != 0:
            self.__server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.__server.bind(("", port))
        else:
            print "Cloud not find myself in startup list"
            sys.exit(-1)

    def sendMembershipList(self):
        self.__me.heartbeat = self.__me.heartbeat + 1

    def getRandomMember(self):
        member = None
        if len(self.__memberList) > 1:
            tries = 10
            while True:
                randomNeighborIndex = random.randint(len(self.__memberList))
                member = self.__memberList[randomNeighborIndex]
                tries -= 1
                if tries <= 0:
                    member = None
                    break
                if member.address == self.__myAddress:
                    break
        else:
            print "I am alone in this world."
        return member

    class MembershipGosspier(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.__keepRunning = true

        def run(self):
            while self.__keepRunning:
                time.sleepTime(self.__t_gossip)
                self.sendMembershipList()

    class AsynchronousReceiver(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.__keepRunning = true

        def run(self):
            while self.__keepRunning:
                buf, addr = self.__server.recvfrom(2048)
                remotelist = pickle.loads(buf)
                self.mergeLists(remotelist)

        def mergeLists(self, remoteList):
            pass

    def start(self):
        gossiper = self.MembershipGosspier()
        reciver = self.AsynchronousReceiver()

    def handleNotification(self):
        pass

if __name__ == '__main__':
    client = Client(("localhosr",0))
    client.start()
