def number_spiral(y, x):
    if y > x:
        base = (y - 1) ** 2
        if y % 2 == 1:
            return base + x
        return base + 2 * y - x

    base = (x - 1) ** 2
    if x % 2 == 1:
        return base + 2 * x - y
    return base + y

def main():
    t = int(input())
    for _ in range(t):
        y, x = map(int, input().split())
        print(number_spiral(y, x))

if __name__ == "__main__":
    main()