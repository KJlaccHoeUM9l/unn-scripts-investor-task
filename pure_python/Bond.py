class Bond:
    def __init__(self, day, name, price, count):
        self.__nominal = 1000

        self.__day = day
        self.__name = name
        self.__price = price
        self.__count = count
        self.__total_cost = int((price / 100.) * self.__nominal * count)

    def get_total_cost(self):
        return self.__total_cost

    def get_total_reward(self, n_days):
        if n_days < self.__day:
            raise ValueError('Incorrect value. N less than day: {} - {}'.format(n_days, self.__day))
        return self.__nominal * self.__count + (n_days + 30 - self.__day) * self.__count - self.__total_cost

    def __str__(self):
        return '{} {} {} {}'.format(self.__day, self.__name, self.__price, self.__count)

    def __repr__(self):
        return 'Bond({})'.format(str(self))
