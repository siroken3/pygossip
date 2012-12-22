#!/usr/bin/env python
import dbus

NM_SERVICE = 'org.freedesktop.NetworkManager'
NM_OPATH   = '/org/freedesktop/NetworkManager'
NM_DSERVICE = "%s.Devices" % NM_SERVICE

def getAllDevices():
    bus = dbus.SystemBus()

    proxy = bus.get_object(NM_SERVICE, NM_OPATH)
    devs = proxy.getDevices(dbus_interface=NM_SERVICE)

    devices = []
    for dev in devs:
        device = bus.get_object(NM_SERVICE, dev)
        devices.append(device.getProperties(NM_DSERVICE))

    return devices

def getDefaultDevice():
    ds = getAllDevices()
    for d in ds:
        if d[10] != '0.0.0.0':
            return d
    
if __name__ == "__main__":
    d = getDefaultDevice()
    print '%s: %s/%s' % (d[1], d[6], d[7])
