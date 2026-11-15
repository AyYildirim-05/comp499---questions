def is_valid(solution, c, r):
    for i in range(c):
        # r = row
        if solution[i] == r or abs(solution[i] - r) == abs(i - c): # horizontal & vertical conflicts
            return False
    return True

def main():
    n = int(input())
    solution = [-1] * n
    c = 0 # column index
    ns = 0 # number of solutions

    while c >= 0:
        solution[c] += 1 # move queen down the column
        while solution[c] < n and not is_valid(solution, c, solution[c]): # still within the border limits & not attacked
            solution[c] += 1
 
        if solution[c] < n: # valid row within boundary
            if c == n - 1: # last column?
                ns += 1  # Solution found; continue to find next valid row at c
            else:
                c += 1
                solution[c] = -1
        else: # reset the current column back
            solution[c] = -1
            c -= 1

    print(ns)

if __name__ == "__main__":
    main()