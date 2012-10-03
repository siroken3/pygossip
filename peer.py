#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import select
import pprint
import sys
import random
import pickle

class GossipService:
    def __init__(self, port, initialPeers):
        self.peers = initialPeers
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind("", port)

    def recvPeer(self):
        rs, ws, xs = select.select([self.sock],[],[])
        for s in rs:
            data, addr = s.recvfrom(2048)
            recvPeers = pickle.loads(data)
            # self.peersとマージ(重複を削除)

    def sendPeer(self):
        sendSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sendSock.bind(("",0))
        for i in range(0, len(self.peers)):
            peer = random.choice(self.peers)
            # TTLを用意して消滅させる
            sendSock.sendto(picket.dumps(self.peers), (peer.host, peer.port))

    def start(self):
        while 1:
            self.recvPeers()
            self.sendPeers()

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port


if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    if (argc != 3):
        print 'Usage: #python %s host port' % argv[0]
        quit()

    host = argv[1]
    port = argv[2]
    print 'initialized host:%s port:%s' % (host, port)
    initialPeers = [Peer('localhost',2000), Peer('localhost',2001), Peer('localhost',2002)]
    service = GossipService(port, initialPeers)
    service.start()
