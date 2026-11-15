import sys

def main():
    inpt = sys.stdin.read().split()
    if not inpt:
        return

    n = int(inpt[0])
    m = int(inpt[1])
    w = list(map(int, inpt[2:2+n]))
    c = list(map(int, inpt[2+n:2+n+m]))
    
    w.sort()
    c.sort()

    lst_w = 0
    lst_c = 0

    out = 0

    while lst_w < n and lst_c < m:
        if w[lst_w] <= c[lst_c]:
            out += 1
            lst_w += 1
            lst_c += 1
        else:
            lst_c += 1

    print(out)


if __name__ == "__main__":
    main()