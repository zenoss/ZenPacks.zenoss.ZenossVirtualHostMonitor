######################################################################
#
# Copyright 2007 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

import os
from Products.CMFCore.DirectoryView import registerDirectory

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenModel.ZenPack import ZenPackBase

class ZenPack(ZenPackBase):
    
    def install(self, app):
        """
        Add transforms to mutate add/change events from the modeler to
        migration events between esx servers.
        """
        ZenPackBase.install(self, app)

        id = 'virtualMachineDetail'
        try:
            self.dmd.zenMenus.More.manage_deleteZenMenuItem((id,))
        except (KeyError, AttributeError):
            pass
        self.dmd.zenMenus.More.manage_addZenMenuItem(
            id,
            action=id,
            description='Guests',
            allowed_classes=('VirtualMachineHost',),
            ordering=5.0)


    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        self.install(app)
