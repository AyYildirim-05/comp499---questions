import sys

def main():
    """Finds the maximum subarray sum with at most one element deleted."""
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    a = [int(x) for x in tokens[1:n+1]]

    dp0 = a[0] # max sum ending at current index with 0 deletions
    dp1 = -float('inf') # max sum ending at current index with 1 deletion
    ans = a[0]

    for i in range(1, n):
        # Must compute dp1 using the old dp0 before overwriting dp0
        # dp1: delete a[i] (use old dp0) or keep a[i] (extend dp1)
        dp1 = max(dp0, dp1 + a[i])
        # dp0: restart at a[i] or extend previous dp0
        dp0 = max(a[i], dp0 + a[i])
        ans = max(ans, dp0, dp1)

    print(ans)

if __name__ == "__main__":
    main()