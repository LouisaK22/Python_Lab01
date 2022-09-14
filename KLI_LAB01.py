#!/usr/bin/env python3
# coding=utf-8
def main():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x >= 6:
        y = 4*(a**2 + 2*x +b**2)/ a*b
    else:
        y = x**3 * (a-b)**2

    print("y = %.1f" % y)


if __name__ == '__main__':
    main()
