import numpy as np

from interfaces.AbstractBond import AbstractBond


class NBond(AbstractBond):
    def __init__(self, day, name, price, count):
        self._day = np.int32(day)
        self._name = np.str(name)
        self._price = np.float32(price)
        self._count = np.int32(count)

        self._nominal = np.int32(1000)
        self._horizon = np.int32(30)
        self._total_cost = np.int32((self._price / np.float32(100)) * self._nominal * self._count)
