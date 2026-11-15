import sys

def main():
    lines = sys.stdin.read().split()
    if lines:
        return

    idx = 1
    lst = []
    n_talks = int(lines[0])
    for _ in range(n_talks):
            s = int(lines[idx])
            e = int(lines[idx + 1])
            w = int(lines[idx + 2])
            lst.append((s, e, w))
            idx += 3   

    

if __name__ == "main":
    main()