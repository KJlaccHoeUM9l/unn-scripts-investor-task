from functools import lru_cache

from interfaces.IOptimizableInvestor import IOptimizableInvestor
from interfaces.AbstractBond import AbstractBond


def dynamic_programming(investor, bonds):
    if not isinstance(investor, IOptimizableInvestor):
        raise TypeError('Incorrect type, investor should implement IOptimizableInvestor interface')
    if len(bonds) == 0:
        raise ValueError('No bonds')
    elif not isinstance(bonds[0], AbstractBond):
        raise TypeError('Incorrect type, every bond should extend AbstractBond class')

    max_money = investor.s_money
    best_rewards = [[0] * (max_money + 1) for _ in range(len(bonds) + 1)]

    for current_bond_index, (bond) in enumerate(bonds, 1):
        reward = bond.get_total_reward(investor.n_days)
        cost = bond.get_total_cost()

        prev_bond_index = current_bond_index - 1
        for current_money in range(max_money + 1):
            if cost > current_money:
                best_rewards[current_bond_index][current_money] = best_rewards[prev_bond_index][current_money]
            else:
                best_rewards[current_bond_index][current_money] = max(best_rewards[prev_bond_index][current_money],
                                                                      best_rewards[prev_bond_index][current_money - cost] + reward)

    available_money = max_money
    for bond_number in reversed(range(1, len(bonds) + 1)):
        if best_rewards[bond_number][available_money] != best_rewards[bond_number - 1][available_money]:
            investor.add_bond((bonds[bond_number - 1]))
            available_money -= bonds[bond_number - 1].get_total_cost()

    investor.reverse_bonds()
    investor.set_total_reward(best_rewards[len(bonds)][max_money])


def dynamic_programming_recursive(investor, bonds):
    if not isinstance(investor, IOptimizableInvestor):
        raise TypeError('Incorrect type, investor should implement IOptimizableInvestor interface')
    if len(bonds) == 0:
        raise ValueError('No bonds')
    elif not isinstance(bonds[0], AbstractBond):
        raise TypeError('Incorrect type, every bond should extend AbstractBond class')

    @lru_cache(maxsize=None)
    def best_reward(num_elements_, available_money_):
        if available_money_ < 0:
            return float('-inf')
        if num_elements_ == 0:
            return 0

        reward = bonds[num_elements_ - 1].get_total_reward(investor.n_days)
        cost = bonds[num_elements_ - 1].get_total_cost()
        return max(best_reward(num_elements_ - 1, available_money_),
                   best_reward(num_elements_ - 1, available_money_ - cost) + reward)

    max_money = investor.s_money
    available_money = max_money
    for bond_number in reversed(range(len(bonds))):
        if best_reward(bond_number + 1, available_money) != best_reward(bond_number, available_money):
            investor.add_bond(bonds[bond_number])
            available_money -= bonds[bond_number].get_total_cost()

    investor.reverse_bonds()
    investor.set_total_reward(best_reward(len(bonds), max_money))
