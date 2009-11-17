###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2009, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

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
