import sys

def main():
    token = sys.stdin.read().split()
    if not token:
        return

    n = int(token[0])

    dp = [float("inf")] * (n + 1)   # dp[i] = the minimum number of steps to reduce i down to 0
    dp[0] = 0

    for i in range(1, n + 1):
        temp = i
        while temp > 0:
            d = temp % 10          # extracts the last digit
            temp = temp // 10      # drops the last digit

            if d != 0:
                # Check if using digit 'd' beats our current best for dp[i]:
                dp[i] = min(dp[i], 1 + dp[i - d])

    print(dp[n])

if __name__ == "__main__":
    main()