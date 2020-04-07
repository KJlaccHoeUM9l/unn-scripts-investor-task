class AbstractBond:
    __slots__ = '_nominal', '_day', '_name', '_price', '_count', '_total_cost'

    def get_total_cost(self):
        return self._total_cost

    def get_total_reward(self, n_days):
        if n_days < self._day:
            raise ValueError('Incorrect value. N less than day: {} - {}'.format(n_days, self._day))
        return self._nominal * self._count + (n_days + 30 - self._day) * self._count - self._total_cost

    def __str__(self):
        return '{} {} {} {}'.format(self._day, self._name, self._price, self._count)

    def __repr__(self):
        return 'Bond({})'.format(str(self))
