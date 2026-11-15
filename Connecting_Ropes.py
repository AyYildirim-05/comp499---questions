import heapq

def main():
    n = int(input())
    lst = list(map(int, input().split()))
    heapq.heapify(lst)
    total_cost = 0

    while len(lst) > 1:
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        cost = first + second
        total_cost += cost
        heapq.heappush(lst, cost)
    print(total_cost)

if __name__ == "__main__":
    main()