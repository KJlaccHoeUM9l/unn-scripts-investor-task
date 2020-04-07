class Investor:
    def __init__(self, n_days, m_items, s_money):
        self.n_days = n_days
        self.m_items = m_items
        self.s_money = s_money

        self.__bonds = []
        self.__total_reward = None

    def add_bond(self, bond):
        if self.s_money - bond.get_total_cost() >= 0:
            self.__bonds.append(bond)
            self.s_money -= bond.get_total_cost()

    def set_total_reward(self, reward):
        self.__total_reward = reward

    def get_profitable_bonds(self):
        return self.__bonds

    def get_total_reward(self):
        return self.__total_reward
