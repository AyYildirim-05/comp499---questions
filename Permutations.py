def main():
    input_data = int(input().strip())
    if not input_data:
        return
    n = int(input_data)

    if n == 1:
        print("1")
        return

    if n == 2 or n == 3:
        print("NO SOLUTION")
        return

    evens = range(2, n + 1, 2)
    odds = range(1, n + 1, 2)

    print(" ".join(map(str, evens)) + " " + " ".join(map(str, odds)))


if __name__ == "__main__":
    main()