def main():
    n = int(input())
    numbers = map(int, input().split())
    total_sum = n * (n + 1) // 2

    actual_sum = sum(numbers)
    
    print(total_sum - actual_sum)

if __name__ == "__main__":
    main()  

