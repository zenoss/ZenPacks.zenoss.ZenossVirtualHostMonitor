######################################################################
#
# Copyright 2008 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPack, ZenPackMigration
from ZenPacks.zenoss.ZenossVirtualHostMonitor.VirtualMachineHost \
        import VirtualMachineHost
from ZenPacks.zenoss.ZenossVirtualHostMonitor.VirtualMachine \
        import VirtualMachine

class ConvertVirtualHosts(ZenPackMigration):
    version = Version(2, 2, 0)

    reIndex = True

    def convert(self, objs, oldClass, newClass):
        for obj in objs:
            if oldClass and newClass and isinstance(obj, oldClass):
                obj.__class__ = newClass
            if self.reIndex and isinstance(obj, newClass):
                obj.index_object()
                
    def getOldClass(self, oldModuleName, oldClassName):
        try:
            exec('import %s' % oldModuleName)
            return eval('%s.%s' % (oldModuleName, oldClassName))
        except ImportError:
            # The old-style code no longer exists in Products,
            # so we assume the migration has already happened.
            return None
    
    def migrate(self, pack):
        try:
            root = pack.dmd.Devices.Server._getOb('Virtual Machine Host')
        except AttributeError:
            return

        oldModuleName = 'Products.ZenossVirtualHostMonitor.VirtualMachineHost'
        oldClassName = 'VirtualMachineHost'
        oldClass = self.getOldClass(oldModuleName, oldClassName)

        objs = root.getSubDevices()
        self.convert(objs, oldClass, VirtualMachineHost)
        
        oldModuleName = 'Products.ZenossVirtualHostMonitor.VirtualMachine'
        oldClassName = 'VirtualMachine'
        oldClass = self.getOldClass(oldModuleName, oldClassName)

        for dev in objs:
            # Only convert guests of hosts that were actually
            # converted in case there are non-VirtualMachineHost
            # devices in the device class (internal #1394)
            if isinstance( dev, VirtualMachineHost ):             
                self.convert(dev.guestDevices(), oldClass, VirtualMachine)
        
