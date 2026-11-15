import sys
import heapq

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    jobs = []
    
    idx = 1
    for _ in range(n):
        d = int(data[idx])
        p = int(data[idx + 1])
        jobs.append((d, p))
        idx += 2

    jobs.sort(key=lambda x: x[0])

    min_heap = []


    for d, p in jobs: # d: deadline p: profit
        if len(min_heap) < d:
            heapq.heappush(min_heap, p)
        elif min_heap and p > min_heap[0]:
            heapq.heapreplace(min_heap, p)

    print(sum(min_heap))

if __name__ == '__main__':
    solve()