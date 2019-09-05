import argparse
import math_lib as ml

def main():
    parser = argparse.ArgumentParser(
                description = 'Parameters for adding and dividing',
                prog = 'the_good_way')

    parser.add_argument('--value_one_add',
                        type = float,
                        help = 'first number to be added',
                        required = True)

    parser.add_argument('--value_two_add',
                        type = float,
                        help = 'second number to be added',
                        required = True)

    parser.add_argument('--value_one_div',
                        type = float,
                        help = 'first number to be divided',
                        required = True)

    parser.add_argument('--value_two_div',
                        type = float,
                        help = 'second number to be divided',
                        required = True)

    args = parser.parse_args()

    print(ml.add(args.value_one_add, args.value_two_add))
    print(ml.div(args.value_one_div, args.value_two_div))
    
if __name__ == '__main__':
    main()