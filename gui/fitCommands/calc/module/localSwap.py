import wx
from logbook import Logger

import eos.db
from eos.exception import HandledListActionError
from service.fit import Fit


pyfalog = Logger(__name__)


class CalcSwapLocalModuleCommand(wx.Command):

    def __init__(self, fitID, position1, position2):
        wx.Command.__init__(self, True, 'Swap Modules')
        self.fitID = fitID
        self.position1 = position1
        self.position2 = position2

    def Do(self):
        pyfalog.debug('Doing swapping between {} and {} for fit {}'.format(self.position1, self.position2, self.fitID))
        self.__swap(self.fitID, self.position1, self.position2)
        return True

    def Undo(self):
        self.__swap(self.fitID, self.position2, self.position1)
        pyfalog.debug('Undoing swapping between {} and {} for fit {}'.format(self.position1, self.position2, self.fitID))
        return True

    def __swap(self, fitID, position1, position2):
        fit = Fit.getInstance().getFit(fitID)
        mod1 = fit.modules[position1]
        mod2 = fit.modules[position2]
        fit.modules.free(position1)
        fit.modules.free(position2)
        try:
            fit.modules.replace(position2, mod1, raiseFailure=True)
        except HandledListActionError:
            fit.modules.replace(position1, mod1)
            fit.modules.replace(position2, mod2)
            eos.db.commit()
            return False
        try:
            fit.modules.replace(position1, mod2, raiseFailure=True)
        except HandledListActionError:
            fit.modules.free(position2)
            fit.modules.replace(position1, mod1)
            fit.modules.replace(position2, mod2)
            eos.db.commit()
            return False
        eos.db.commit()
        return True
