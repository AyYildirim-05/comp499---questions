import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    c = int(input_data[0]) # number of coins
    m = int(input_data[1]) # target

    x = [int(x) for x in input_data[2 : 2 + c]] # coins

    s =[-1 for _ in range(m+1)] # min coin needed to mkae a coin

    s[0] =0

    for i in range(1, m+1):
        for j in range(0, c):
            if i < x[j] or s[i - x[j]]<0:
                continue
            a = 1 + s[i - x[j]] # total coins
            # s[i - coin] (the minimum coins needed for the rest of the amount)
            if s[i] == -1 or s[i] > a: # empty spot or uses fewer coins compared to previous
                    s[i] = a

    print(s[m])

if __name__ == "__main__":
    main()