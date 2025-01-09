import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', type=str, default='default_value')
    parser.add_argument('--arg2', type=int, default=0)
    return parser.parse_args()