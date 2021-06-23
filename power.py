from math import pow


def potence(n, *args):
    n2 = args[0]
    if args:
        print(pow(n, n2))
    else:
        print(pow(n, 2))


def main():
    n = int(input('give me the number:'))
    n2 = input('give me the power or not, is optional:')
    if n2 == '':
        potence(n)
    else:
        potence(n, int(n2))


if __name__ == '__main__':
    main()
