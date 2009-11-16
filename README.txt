Zenoss Virtual Host Monitor
---------------------------

ZenossVirtualHostMonitor is a ZenPack that allows you to monitor
virtually hosted operating systems.  This ZenPack refers to a Virtual
Machine Host as the one running on the bare metal, and Guest for those
running within the virtual hardware.

This zenpack:

     1) Extends Devices to support a relationship from Host to Guest.

     2) Provides screens displaying resources allocated to Guest OSs.

     3) Collects nothing on its one.  It provides base functionality
        for other zenpacks (XenMonitor, VMwareESXMonitor)