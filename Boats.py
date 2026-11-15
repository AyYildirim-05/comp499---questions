import sys

def main():
    inpt = sys.stdin.read().split()
    if not inpt:
        return

    n = int(inpt[0])
    limit = int(inpt[1])
    weights = sorted(int(x) for x in inpt[2:2 + n])

    left = 0
    right = n - 1
    boats = 0

    while left <= right:
        if left < right and weights[left] + weights[right] <= limit:
            left += 1
        
        # The heaviest person always takes a spot on this boat
        right -= 1
        boats += 1

    print(boats)

if __name__ == "__main__":
    main()