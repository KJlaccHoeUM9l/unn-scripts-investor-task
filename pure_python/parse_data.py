from pure_python.Investor import Investor
from pure_python.Bond import Bond


def parse(file_path):
    with open(file_path) as f:
        n_days, m_items, s_money = f.readline().split()
        investor = Investor(int(n_days), int(m_items), int(s_money))
        bonds = []
        for line in f:
            day, name, price, count = line.split()
            bonds.append(Bond(int(day), str(name), float(price), int(count)))

    return investor, bonds
