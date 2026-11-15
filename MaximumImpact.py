from bisect import bisect_right
import sys


def main():
  tokens = sys.stdin.read().split()
  if not tokens:
    return

  n = int(tokens[0])
  talks = []

  idx = 1
  for _ in range(n):
    s = int(tokens[idx])
    e = int(tokens[idx + 1])
    w = int(tokens[idx + 2])
    talks.append((s, e, w))
    idx += 3

  talks.sort(key=lambda talk: talk[1])

  end_times = [talk[1] for talk in talks]

  dp = [0] * (n + 1)

  for i in range(1, n + 1):
    s_i, e_i, w_i = talks[i - 1]
    k = bisect_right(end_times, s_i, 0, i - 1)

    #Skip talk i -> dp[i - 1]
    #Take talk i -> dp[k] + w_i
    dp[i] = max(dp[i - 1], dp[k] + w_i)

  print(dp[n])


if __name__ == "__main__":
  main()