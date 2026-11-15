import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    x = int(input_data[1])
    coins = [int(v) for v in input_data[2 : 2 + n]]

    dp  = [float("inf")] * (x + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, x + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    if dp[x] == float("inf"):
        print(-1)
    else:
        print(dp[x])      


if __name__ == "__main__":
    main()