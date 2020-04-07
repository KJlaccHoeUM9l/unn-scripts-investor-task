from abc import ABC, abstractmethod


class IOptimizableInvestor(ABC):
    @abstractmethod
    def add_bond(self, bond):
        pass

    @abstractmethod
    def reverse_bonds(self):
        pass

    @abstractmethod
    def get_profitable_bonds(self):
        pass

    @abstractmethod
    def set_total_reward(self, reward):
        pass

    @abstractmethod
    def get_total_reward(self):
        pass
