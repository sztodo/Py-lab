def sume(n):
    s = 0
    i = 1
    while s <= n:
        i = i + 1
        s = i * (i - 1)//2
        p = n - s
        if (p > 0) and (p % i == 0):
            for j in range(i):
                print(p//i + j, end=' ')
            print('\n')


if __name__ == "__main__":
    n = int(input('n='))
    sume(n)

