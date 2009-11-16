######################################################################
#
# Copyright 2007 Zenoss, Inc.  All Rights Reserved.
#
######################################################################
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
