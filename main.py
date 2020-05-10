import os
import time

import optimization_algorithms

from args import parse_args
from pure_python import parse_data
from with_numpy_types import n_parse_data


def main(output_path, investor, bonds, algorithm, use_cache=True):
    elapsed_time = time.time()
    try:
        algorithm(investor, bonds, use_cache=use_cache)
    except TypeError:
        algorithm(investor, bonds)
    elapsed_time = time.time() - elapsed_time

    print('Elapsed time: {:.2f} ms'.format(elapsed_time * 1000))

    with open(output_path, 'w') as f:
        f.write('{}\n'.format(investor.get_total_reward()))
        for bond in investor.get_profitable_bonds():
            f.write('{}\n'.format(bond))
    print('Results have been saved to {}'.format(output_path))


if __name__ == '__main__':
    __args = parse_args()

    # Parse input path
    __input_path = __args.i
    if not os.path.isfile(__input_path):
        raise ValueError('Input error, file "{}" doesn\'t exists.'.format(__input_path))

    # Parse output path
    __output_path = __args.o
    if not os.path.isdir(__output_path):
        raise ValueError('Output error, directory "{}" doesn\'t exists.'.format(__output_path))
    __output_path = os.path.join(__output_path, 'output.txt')

    # Parse algorithm type
    __algorithm_type = __args.a
    if __algorithm_type == 'base':
        __algorithm = optimization_algorithms.dynamic_programming
        __use_cache = False
    elif __algorithm_type == 'base_recursive':
        __algorithm = optimization_algorithms.dynamic_programming_recursive
        __use_cache = False
    else:
        __algorithm = optimization_algorithms.dynamic_programming_recursive
        __use_cache = True

    # Parse NumPy types mode
    __use_numpy = __args.use_numpy_types
    if __use_numpy == 0:
        data_parser = parse_data
    else:
        data_parser = n_parse_data

    # Run program
    __investor, __bonds = data_parser.parse(__input_path)
    main(__output_path, __investor, __bonds, __algorithm, __use_cache)
