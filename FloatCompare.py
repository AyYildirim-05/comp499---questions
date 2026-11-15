
import sys
def main():
    lines = sys.stdin.read().splitlines()

    if lines:
        n = int(lines[0])
        for n in lines[1:n + 1]:
            val = float(n)
            if val == 0:
                print("-inf" if str(n).startswith("-") else "inf")
            else:
                print(f"{1.0 / val:.9g}")


if __name__ == "__main__":
    main()