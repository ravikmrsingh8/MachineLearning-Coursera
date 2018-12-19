def apply(func, x):
    print(func(x))


if __name__ == "__main__":
    apply(lambda x : x ** 2, 4)
    apply(lambda x : x ** 3, 4)
    apply(lambda x : -x, -4)
