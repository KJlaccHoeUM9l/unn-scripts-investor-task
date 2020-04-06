import os

from Bond import Bond
from Investor import Investor

import utils
import optimization_algorithms

if __name__ == '__main__':
    # test_file_path = os.path.join('test_files', 'first_test.txt')
    # test_file_path = os.path.join('test_files', 'random_data_medium.txt')
    test_file_path = os.path.join('test_files', 'random_data_small.txt')

    investor, bonds = utils.parse(test_file_path)

    # optimization_algorithms.dynamic_programing(investor, bonds)
    optimization_algorithms.dynamic_programming_recursive(investor, bonds)

    print(investor.get_total_reward())
    for bond in investor.bonds:
        print(bond)
