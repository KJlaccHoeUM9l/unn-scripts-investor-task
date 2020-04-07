from functools import lru_cache


def dynamic_programming_recursive(investor, bonds):
    # @lru_cache(maxsize=None)
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

    investor.get_profitable_bonds().reverse()
    investor.set_total_reward(best_reward(len(bonds), max_money))
