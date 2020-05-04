import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
            '-a',
            default='opt',
            type=str,
            help='Search algorithm (base | base_recursive | opt)',
            required=False
    )
    parser.add_argument(
            '-i',
            type=str,
            help='Path to input file',
            required=True
    )
    parser.add_argument(
            '-o',
            type=str,
            help='Path to output directory',
            required=True
    )
    parser.add_argument(
            '-use_numpy_types',
            type=int,
            default=0,
            help='Use numpy types for input data (0 | 1)',
            required=False
    )

    return parser.parse_args()
