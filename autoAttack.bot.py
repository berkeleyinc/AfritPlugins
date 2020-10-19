## Attacks selected/locked targets
import base 
from botapi import *

def CreateBot():
    return AutoAttackBot()

################################################################

class AutoAttackBot(base.BotBase):
    def __init__(self):
        base.BotBase.__init__(self, 'autoAttack')

    def onBotLoopStart(self):
        print("AutoAttack loaded.")
    def onHeroTargetUpdate(self):
        print("Hero target changed from " + str(self.old_map.hero.selectedTarget) + " to " + str(self.new_map.hero.selectedTarget))
        if self.new_map.hero.selectedTarget != 0:
            # Attack any ship that your ship selected:
            ship = GetShipByUid(self.new_map.ships, self.new_map.hero.selectedTarget);
            if (ship is None):
                return
            print("Attack " + ship.serialize())
            self.acts.attackShip(ship)
