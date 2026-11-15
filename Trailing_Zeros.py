def main():
    n = int(input())
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
        
    print(zeros)
    

if __name__ == "__main__":
    main()