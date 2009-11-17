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

import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPack
import logging
log = logging.getLogger('zenpack')

class Menu:
    version = Version(2, 2, 1)

    def migrate(self, pack):
        log.info('installing Guest menu item')
        dmd = pack.__primary_parent__.__primary_parent__
        id = 'virtualMachineDetail'
        try:
            dmd.zenMenus.More.manage_deleteZenMenuItem((id,))
        except (KeyError, AttributeError):
            pass
        dmd.zenMenus.More.manage_addZenMenuItem(
            id,
            action=id,
            description='Guests',
            allowed_classes=('VirtualMachineHost',),
            ordering=5.0)
        log.info('installed Guest menu item')
                     
Menu()
