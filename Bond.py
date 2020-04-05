class Bond:
    def __init__(self, day, name, price, count):
        self.nominal = 1000

        self.day = day
        self.name = name
        self.price = price
        self.count = count
        self.total_cost = int((price / 100.) * self.nominal * count)
        # self.total_reward = (self.nominal * count + (day + 30) * self.count) - self.total_cost

    def get_total_reward(self, n_days):
        if n_days < self.day:
            raise ValueError('Incorrect value. N less than day: {} - {}'.format(n_days, self.day))

        return self.nominal * self.count + (n_days + 30 - self.day) * self.count - self.total_cost

    def __str__(self):
        return '{} {} {} {}'.format(self.day, self.name, self.price, self.count)

    def __repr__(self):
        return 'Bond({})'.format(str(self))
