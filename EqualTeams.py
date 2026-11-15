
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    N = int(data[0])
    K = int(data[1])
    lst = [int(x) for x in data[2:2 + N]]

    s = sum(lst)
    if s % K != 0:
        print("NO")
        return

    target = s // K
    lst.sort(reverse=True)
    bits = 1  

    if lst[0] > target:
        print("NO")
        return

    buckets = [0] * K

    def backtrack(idx):
        if idx == N:
            return True

        val = lst[idx]
        for i in range(K):
            if buckets[i] + val <= target:
                buckets[i] += val
                if backtrack(idx + 1):
                    return True
                buckets[i] -= val

            if buckets[i] == 0:
                break

        return False

    if backtrack(0):
        print("YES")
    else:
        print("NO") 
    
if __name__ == "__main__":
    main()