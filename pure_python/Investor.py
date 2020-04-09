from interfaces.IOptimizableInvestor import IOptimizableInvestor


class Investor(IOptimizableInvestor):
    def __init__(self, n_days, m_bonds, s_money):
        self.n_days = n_days
        self.m_bonds = m_bonds
        self.s_money = s_money

        self.__bonds = []
        self.__total_reward = None

    def add_bond(self, bond):
        if self.s_money - bond.get_total_cost() >= 0:
            self.__bonds.append(bond)
            self.s_money -= bond.get_total_cost()

    def reverse_bonds(self):
        self.__bonds.reverse()

    def get_profitable_bonds(self):
        return self.__bonds

    def set_total_reward(self, reward):
        self.__total_reward = reward

    def get_total_reward(self):
        return self.__total_reward
