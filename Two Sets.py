def main():
    n = int(input())
    total_sum = n * (n + 1) // 2

    if total_sum % 2 != 0:
        print("NO")
        return

    print("YES")
    A = []
    B = []
    start = 1
    if n % 4 == 3:
        A.extend([1, 2])
        B.append(3)
        start = 4

    for a in range(start, n + 1, 4):
        A.extend([a, a + 3])
        B.extend([a + 1, a + 2])
    print(len(A))
    print(*A)
    print(len(B))
    print(*B) #  unpacks the items inside the collection

if __name__ == "__main__":
    main()
    