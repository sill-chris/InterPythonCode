def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


if __name__ == '__main__':
    square = raise_to(2)
    print(square(5))
    print(square.__closure__)
    print(square(9))

    cubed = raise_to(3)
    print(cubed(2))
    print(cubed(3))