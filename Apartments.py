import sys

# problem of matching 2 different lists of apartments and applicants with a given tolerance k (same question as in lab)

def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    m = int(tokens[1])
    k = int(tokens[2])
    a = list(map(int, tokens[3:n+3]))
    b = list(map(int, tokens[n+3:]))

    a.sort()
    b.sort()
    count = 0
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) > k:
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        else:
            count += 1
            i += 1
            j += 1

    print(count)
if __name__ == "__main__":
    main()