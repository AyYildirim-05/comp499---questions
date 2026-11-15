def main():
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))

    lst.sort(key=lambda x: x[1])

    out = 0
    last_end = -1

    for start, end in lst:
        if start >= last_end:
            out += 1
            last_end = end

    print(out)

if __name__ == "__main__":
    main()