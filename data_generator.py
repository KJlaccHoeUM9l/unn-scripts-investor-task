import os
import random
import string


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def generate_data(n_days, m_lots, s_money, file_path):
    with open(file_path, 'w') as f:
        f.write('{} {} {}\n'.format(n_days, m_lots, s_money))
        for day in range(1, n_days + 1):
            num_lots = random.randint(0, m_lots)
            for lot in range(1, num_lots + 1):
                f.write('{} {} {} {}\n'.format(day,
                                               generate_random_string(random.randint(7, 47)),
                                               random.uniform(47, 147),
                                               random.randint(5, 47)))


def main():
    file_path = os.path.join('test_files', 'random_data_small.txt')
    generate_data(n_days=27, m_lots=7, s_money=14747, file_path=file_path)


if __name__ == '__main__':
    main()
