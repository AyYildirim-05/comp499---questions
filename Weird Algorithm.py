def main():
    n = int(input())
    weird_algorithm(n)

def weird_algorithm(x):
    print(x, end=" ")
    if x == 1:
        return
    if x % 2 == 0:
        weird_algorithm(x // 2)
    else:
        weird_algorithm(3 * x + 1)

if __name__ == "__main__":
    main()