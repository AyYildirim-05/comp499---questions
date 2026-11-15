import sys

def main():

    token = sys.stdin.read().split()
    if not token:
        return

    n = int(token[0]) # number of coins
    m = int(token[1]) # target
    coins = [int(x) for x in token[2:]]

    INF = float("inf")
    dp = [INF] * (m + 1) # dp[s] will hold the minimum number of coins needed to make sum s holds 0 to m (m indices)
    dp[0] = 0

    for c in coins:
        if c > m:
          continue
        # Traverse backwards so each coin is only used once
        for s in range(m, c - 1, -1): # s is the current sum we are trying to make
            if dp[s - c] != INF:
                dp[s] = min(dp[s], dp[s - c] + 1)
        # dp[s] the minimum number of coins needed to make sum s using the current coin c
        # dp[s - c] + 1 is the number of coins needed to make sum s - c plus the current coin c
    if dp[m] != INF:
        print(dp[m])
    else:
        print(-1)

if __name__ == "__main__":
    main()