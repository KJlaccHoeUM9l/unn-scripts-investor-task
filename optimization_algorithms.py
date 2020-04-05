from Investor import Investor


def dynamic_programing(investor, bonds):
    if isinstance(investor, Investor):
        def knapsack(W, wt, val, n):
            K = [[0 for x in range(W + 1)] for x in range(n + 1)]

            for i in range(n + 1):
                for w in range(W + 1):
                    if i == 0 or w == 0:
                        K[i][w] = 0
                    elif wt[i - 1] <= w:
                        K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],
                                      K[i - 1][w])
                    else:
                        K[i][w] = K[i - 1][w]
            # K[n][W]
            return K

        def find_ans(k, s):
            if _best_reword_matrix[k][s] == 0:
                return
            if _best_reword_matrix[k - 1][s] == _best_reword_matrix[k][s]:
                find_ans(k - 1, s)
            else:
                find_ans(k - 1, s - total_cost[k])
                _answer_indexes.append(k)

        total_reward = [bond.get_total_reward(investor.n_days) for bond in bonds]
        total_cost = [bond.total_cost for bond in bonds]
        investor_money = investor.s_money
        count_papers = len(total_cost)

        _best_reword_matrix = knapsack(investor_money, total_cost, total_reward, count_papers)
        _answer_indexes = []

        find_ans(count_papers, investor_money)

        investor.total_reward = _best_reword_matrix[count_papers][investor_money]
        for i in _answer_indexes:
            investor.bonds.append(bonds[i - 1])
