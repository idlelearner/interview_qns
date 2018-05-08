def print_l(*args):
    for v in enumerate(args):
        print v

if __name__ == '__main__':
    print_l(1,2,2,4)