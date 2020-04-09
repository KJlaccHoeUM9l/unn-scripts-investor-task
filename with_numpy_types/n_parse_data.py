import numpy as np

from with_numpy_types.NInvestor import NInvestor
from with_numpy_types.NBond import NBond


def parse(file_path):
    with open(file_path) as f:
        n_days, m_items, s_money = f.readline().split()
        investor = NInvestor(np.int32(n_days), np.int32(m_items), np.int32(s_money))
        bonds = np.empty(0, dtype=NBond)
        for line in f:
            day, name, price, count = line.split()
            bonds = np.append(bonds, NBond(np.int32(day), np.str(name), np.int32(float(price)), np.int32(count)))

    return investor, bonds
