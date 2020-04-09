from interfaces.AbstractBond import AbstractBond


class Bond(AbstractBond):
    def __init__(self, day, name, price, count):
        self._day = day
        self._name = name
        self._price = price
        self._count = count

        self._nominal = 1000
        self._horizon = 30
        self._total_cost = int((self._price / 100.) * self._nominal * self._count)
