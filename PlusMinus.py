import sys

def main():
    token = sys.stdin.read().split()
    if not token:
        return

    n = int(token[0])
    t = int(token[1])
    arr = list(map(int, token[2:2+n]))

    def canReach(idx, c_sum):
        if idx == n:
            return c_sum == t
        
        return canReach(idx + 1, c_sum + arr[idx]) or canReach(idx + 1, c_sum - arr[idx])

    if canReach(0, 0):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
