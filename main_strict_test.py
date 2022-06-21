import argparse
from src import yp_data_preprocess, gnn_train
import torch
import numpy as np

def print_setting(args):
    print('\n===========================')
    for k, v, in args.__dict__.items():
        print('%s: %s' % (k, v))
    print('===========================\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type=int, default=5, help='the index of gpu device')

    parser.add_argument('--dataset', type=str, default='test', help='')
    parser.add_argument('--pretrained', type=str, default='./pretrain/saved/cmpnn_1024', help='pretrained model path')

    parser.add_argument('--epochs', type=int, default=5000, help='number of epochs')
    parser.add_argument('--batch_size', type=int, default=128, help='batch size')
    parser.add_argument('--lr', type=float, default=1e-4, help='learning rate')
    parser.add_argument('--decay', type=float, default=0.02, help='decay')
    parser.add_argument('--seed', type=int, default=0, help='seed')
    parser.add_argument('--save', type=bool, default=False, help='save model')

    args = parser.parse_args()
    print_setting(args)
    args.test = 1
    np.random.seed(args.seed)
    data = yp_data_preprocess.load_data(args, 'strict_test')
    gnn_train.test_external(args, data)

if __name__ == '__main__':
    main()