import os

from Bond import Bond
from Investor import Investor

import utils
import optimization_algorithms

if __name__ == '__main__':
    # test_file_path = os.path.join('test_files', 'first_test.txt')
    test_file_path = os.path.join('test_files', 'random_data.txt')

    investor, bonds = utils.parse(test_file_path)

    optimization_algorithms.dynamic_programing(investor, bonds)
    print(investor.get_total_reward())
