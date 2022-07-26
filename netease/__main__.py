import sys
from .netease import historical_prices
import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('cmd', help='Command', nargs='?', default='history')
    parser.add_argument('--code', nargs='?', default='0600000', help='股票代码 0600000')
    parser.add_argument('--start', nargs='?', default='20220323', help='开始时间 20220323')
    parser.add_argument('--end', nargs='?', default='20220323', help='结束时间 20220323')
    args=parser.parse_args()

    if args.cmd == 'history':
        print(historical_prices(args.code, args.start, args.end))
