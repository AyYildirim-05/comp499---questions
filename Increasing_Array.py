def main():
    n = int(input())
    lst = list(map(int, input().split()))
    
    moves = 0
    for i in range(1, n):
        if lst[i] < lst[i - 1]:
            moves += lst[i - 1] - lst[i]
            lst[i] = lst[i - 1]
            
    print(moves)

if __name__ == "__main__":
    main()