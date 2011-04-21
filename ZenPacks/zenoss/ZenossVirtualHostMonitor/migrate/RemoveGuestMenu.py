###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

import logging
log = logging.getLogger('zenpack.ZenossVirtualHostMonitor')

import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPack

class RemoveGuestMenu:
    version = Version(3, 1, 0)

    def migrate(self, pack):
        log.info('Removing Guest menu item')
        dmd = pack.__primary_parent__.__primary_parent__
        id = 'virtualMachineDetail'
        moreMenuIds = [menu.id for menu in dmd.zenMenus.More.objectValues()]
        if id in moreMenuIds:
            try:
                dmd.zenMenus.More.manage_deleteZenMenuItem((id,))
            except (KeyError, AttributeError):
                pass
                     
RemoveGuestMenu()
