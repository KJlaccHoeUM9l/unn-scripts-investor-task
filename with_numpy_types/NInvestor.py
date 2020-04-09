import numpy as np

from with_numpy_types.NBond import NBond
from interfaces.IOptimizableInvestor import IOptimizableInvestor


class NInvestor(IOptimizableInvestor):
    def __init__(self, n_days, m_bonds, s_money):
        self.n_days = np.int32(n_days)
        self.m_bonds = np.int32(m_bonds)
        self.s_money = np.int32(s_money)

        self.__bonds = np.empty(0, dtype=NBond)
        self.__total_reward = np.int32(-1)

    def add_bond(self, bond):
        if self.s_money - bond.get_total_cost() >= 0:
            self.__bonds = np.append(self.__bonds, bond)
            self.s_money -= bond.get_total_cost()

    def reverse_bonds(self):
        self.__bonds = self.__bonds[::-1]

    def get_profitable_bonds(self):
        return self.__bonds

    def set_total_reward(self, reward):
        self.__total_reward = np.int32(reward)

    def get_total_reward(self):
        return self.__total_reward
