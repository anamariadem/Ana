from domain import RationalNumber

class Calculator:
    def __init__(self):
        self._total = RationalNumber(0)
        self._history = []

    def add(self,rational):
        '''
        adds a rat num to the total
        :param rational:
        :return:
        '''
        if rational == RationalNumber(0):
            return
        self._history.append(self._total)
        self._total += rational

    def reset(self):
        self._total = RationalNumber(0)

    def undo(self):
        if len(self._history) == 0:
            raise ValueError("No more undos!")
        self._total = self._history.pop()

    def count(self):
        return RationalNumber.noOfInstances()
    @property
    def Total(self):
        return self._total