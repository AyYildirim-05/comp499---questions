import sys

def main():
    tokens = sys.stdin.readline().split()
    first_line = tokens
    if not first_line:
        return
    
    N = int(first_line[0])
    M = int(first_line[1])
    G = sorted(map(int, sys.stdin.readline().split()))
    C = sorted(map(int, sys.stdin.readline().split()))

    child_idx = 0
    candy_idx = 0

    while child_idx < N and candy_idx < M:
        if C[candy_idx] >= G[child_idx]:
            child_idx += 1
        
        candy_idx += 1

    print(child_idx)

if __name__ == "__main__":
    main()