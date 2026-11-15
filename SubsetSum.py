
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    target = int(data[1])
    lst = list(map(int, data[2:2 + n]))

    def can_reach_target(index: int, current_sum: int) -> bool:
        if current_sum == target:
            return True

        if current_sum > target:
            return False

        if index == n:
            return False

        if can_reach_target(index + 1, current_sum + lst[index]):
            return True

        return bool(can_reach_target(index + 1, current_sum))

    if can_reach_target(0, 0):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()