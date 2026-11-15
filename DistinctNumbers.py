import sys

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    n = int(tokens[0])

    arr = list(map(int, tokens[1:1 + n]))

    arr.sort()

    start = 0
    count = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            new_s = i - start
            count +=1 
            start = i

    print(count)
if __name__ == "__main__":
    main()