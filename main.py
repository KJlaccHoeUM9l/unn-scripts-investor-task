import os
import time

from pure_python import parse_data
from with_numpy_types import n_parse_data
import optimization_algorithms

if __name__ == '__main__':
    # test_file_path = os.path.join('test_files', 'random_data_medium.txt')
    test_file_path = os.path.join('test_files', 'random_data_small.txt')

    investor, bonds = parse_data.parse(test_file_path)
    n_investor, n_bonds = n_parse_data.parse(test_file_path)

    default_version = time.time()
    optimization_algorithms.dynamic_programming_recursive(investor, bonds)
    default_version = time.time() - default_version

    fast_version = time.time()
    optimization_algorithms.dynamic_programming_recursive(n_investor, n_bonds)
    fast_version = time.time() - fast_version

    print('Default: {:.2f} ms\n'
          'Fast: {:.2f} ms\n'
          'Acceleration: {:.2f}'.format(default_version * 1000,
                                        fast_version * 1000,
                                        default_version / fast_version))

    print('************* Default **************')
    print(investor.get_total_reward())
    for bond in investor.get_profitable_bonds():
        print(bond)

    print('*********** Optimization ***********')
    print(n_investor.get_total_reward())
    for bond in n_investor.get_profitable_bonds():
        print(bond)
