import sys

def main():
    tk = sys.stdin.read().split()
    n = int(tk[0])
    x = int(tk[1])
    arr = list(map(int, tk[2:]))


    arr.sort()

    end = len(arr) - 1
    start = 0

    count = 0

    while end >= start:
        if start == end:
            count += 1
            break
        if arr[end] + arr[start] <= x:
            end -= 1
            start += 1
            count += 1
        else:
            count += 1
            end -= 1

    print(count)
if __name__ == "__main__":
    main()