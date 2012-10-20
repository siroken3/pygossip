# -*- coding: utf-8 -*-

import sys
import socket
import pickle
import threading
import member as mem
import timeouttimer
import time

class Client:

    def __init__(self, startupHostsList):
        self.__memberList = []
        self.__deadList = []
        self.__t_gossip = 1000
        self.__t_cleanup = 10000
        port = 0
        myIpAddress = self.getMyIpAddress('192.168.0.0')
        self.__myAddress =  (myIpAddress, port)

        for host in startupHostsList:
            member = mem.Member(host, 0, self, self.__t_cleanup)
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

        self.__deadListCond = threading.Condition()
        self.__memberListCond = threading.Condition()

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

    def getMyIpAddress(self, target):
        ipaddr = ''
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((target, 0))
            ipaddr = s.getsockname()[0]
            s.close()
        except:
            pass
        return ipaddr

    class MembershipGosspier(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.__keepRunning = true

        def run(self):
            while self.__keepRunning:
                time.sleepTime(Client.self.__t_gossip)
                Client.self.sendMembershipList()

    class AsynchronousReceiver(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.__keepRunning = true

        def run(self):
            while self.__keepRunning:
                buf, addr = Client.self.__server.recvfrom(2048)
                remotelist = pickle.loads(buf)
                self.mergeLists(remotelist)

        def mergeLists(self, remoteList):
            with Client.self.__deadListCond:
                with Client.self.__memberListCond:
                    for remoteMember in remotelist:
                        if remoteMember in Client.self.__memberList:
                            localMember = Client.self.__memberList[Client.self.__memberList.index(remoteMember)]
                            if remoteMember.heartbeat > localMember.heartbeat:
                                # update local list with latest heatbeat
                                localmember.heartbeat = remoteMember.heartbeat
                                # and reset the timeout of that member
                                localMember.resetTimeoutTimer()
                        else:
                            # the local list does not contain the remote member

                            # the remote member is either brand new, or a previously declared dead member
                            # if its dead, check the heatbeat because it may have come back from the dead
                            if remoteMember in Client.self.__deadList:
                                localDeadMember = Client.self.__deadList[Client.self.__deadList.index(remoteMember)]
                                if remoteMember.heartbeat > localDeadMember.heartbeat:
                                    # its baa-aack
                                    del Client.self.__deadList[Client.self.__deadList.index(remoteMember)]
                                    newLocalMember = Member(remoteMember.address, remoteMember.heartbeat, Client.self, Client.self.__t_cleanup)
                                    Client.self.__memberList.append(newLocalMember)
                                    newLocalMember.startTimeoutTimer()
                                else:
                                    pass # else ignore
                            else:
                                # brand spanking new member - welcome
                                newLocalMember = Member(remoteMember.address, remoteMember.heartbeat, Client.self, Client.self.__t_cleanup)
                                Client.self.__memberList.append(newLocalMember)
                                newLocalMember.startTimeoutTimer()

    def start(self):
        # Start all timers except for me
        for member in self.__memberList:
            if member != self.__me:
                member.startTimeoutTimer()

        gossiper = self.MembershipGosspier()
        gossiper.start()
        reciver = self.AsynchronousReceiver()
        reciver.start()

        while True:
            time.sleepTime(10)

    def handleNotification(self):
        pass

if __name__ == '__main__':
    client = Client([("192.168.0.7",0)])
    client.start()
