def my_pow(x, y):
    return x ** y

if __name__ == '__main__':
    x, y, exp = 2, 5, 32
    ans = my_pow(x, y)
    print(f"Test my_pow({x}, {y}) -> {ans}, exp: {ans} ----", end= "" )

    if ans == exp:
        print("Test OK")
    else:
        print("Test Fail")
