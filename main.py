import os

from pure_python import parse_data
import optimization_algorithms

if __name__ == '__main__':
    # test_file_path = os.path.join('test_files', 'random_data_medium.txt')
    test_file_path = os.path.join('test_files', 'random_data_small.txt')

    investor, bonds = parse_data.parse(test_file_path)
    optimization_algorithms.dynamic_programming_recursive(investor, bonds)
    print(investor.get_total_reward())
    for bond in investor.bonds:
        print(bond)
