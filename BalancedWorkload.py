import sys

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    k = int(tokens[1])
    p = [int(x) for x in tokens[2:2 + n]]

    p.sort(reverse=True)

    def can_fit(max_cap):
        loads = [0] * k

        def backtrack(job_idx):
            if job_idx == n:
                return True

            job_val = p[job_idx]

            for w in range(k):
                if loads[w] + job_val <= max_cap:
                    loads[w] += job_val
                    if backtrack(job_idx + 1):
                        return True
                    loads[w] -= job_val  
                if loads[w] == 0:
                    break

            return False

        return backtrack(0)

    low = p[0]       # largest single element (since sorted descending)
    high = sum(p)    # all elements assigned to one worker
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_fit(mid):
            ans = mid
            high = mid - 1   # Try to find an even smaller maximum load
        else:
            low = mid + 1    # Capacity was too small, need to increase

    print(ans)

if __name__ == "__main__":
    main()