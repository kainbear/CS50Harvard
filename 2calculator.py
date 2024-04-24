def main():
    x = int(input("What's x? "))
    print("x squared is ", square(x))
    print(lox())


def square(n):
    return pow(n, 2)


def lox():
    return 0


main()
