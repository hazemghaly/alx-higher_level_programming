#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    operators = ['+', '-', "*", '/']
    n = len(sys.argv)
    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    operator = sys.argv[2]
    print(operator)
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
    if sys.argv[1].isnumeric() and sys.argv[3].isnumeric():
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    from calculator_1.py import add, sub, mul, div
    if operator == '+':
        print('{} {} {} = {}'.format(a, operator, b, add(a, b)))
    if operator == '-':
        print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))
    if operator == '*':
        print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))
    if operator == '/':
        print('{} {} {} = {}'.format(a, operator, b, div(a, b)))
