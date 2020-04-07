class Investor:
    def __init__(self, n_days, m_items, s_money):
        self.n_days = n_days
        self.m_items = m_items
        self.s_money = s_money

        self.bonds = []
        self.total_reward = None

    def add_bond(self, bond):
        if self.s_money - bond.get_total_cost() >= 0:
            self.bonds.append(bond)
            self.s_money -= bond.get_total_cost()

    def get_total_reward(self):
        if self.total_reward is not None:
            return self.total_reward
        total_reward = 0
        for bond in self.bonds:
            total_reward += bond.get_total_reward(self.n_days)
        return total_reward
