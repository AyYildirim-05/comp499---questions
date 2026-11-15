import sys

def main():
    lines = sys.stdin.read().split()
    if not lines:
        return

    s = lines[0]
    t = lines[1]

    n = len(s)
    m = len(t)

    # dp[i][j] stores the LCS length of s[:i] and t[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # ignore s, ignore t

    print(dp[n][m])

if __name__ == "__main__":
    main()