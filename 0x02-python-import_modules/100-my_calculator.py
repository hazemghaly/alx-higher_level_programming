#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    n = len(sys.argv)
    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and / ")
        sys.exit(1)
    print('{} {} {} = {}'.format(a, operator, b, ops[operator](a, b)))
