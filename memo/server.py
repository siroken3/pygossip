import socket
import select
import pprint

port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print "waiting on port:" , port

rlist=[s]
wlist=[]
xlist=[]

while 1:
#    rs, ws, xs = select.select(rlist, wlist, xlist)
#    for s in rs:
    data, addr = s.recvfrom(1024)
    pprint.pprint((data, addr))
