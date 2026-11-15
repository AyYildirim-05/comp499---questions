import sys

def main():
    token = sys.stdin.read().split()
    if not token:
        return

    n = int(token[0]) # Number of scores
    scores = list(map(int, token[1:])) # List of scores

    dp = [1] * n # dp[i] represents the length of the longest rising score sequence ending at index i

    for i in range(1, n):
        for j in range(i):
            if scores[i] > scores[j]: # Curr_score > prev_score => can extend the rising sequence
                dp[i] = max(dp[i], dp[j] + 1) # Curr_score vs Score of past score + 1

    print(max(dp)) # Maximum length of rising score sequence

if __name__ == "__main__":
    main()