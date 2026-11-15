def main():
    s = input().strip()
    if not s:
        return

    count_A = 0
    count_B = 0
    count_C = 0
    ans = 0

    for ch in s:
        if ch == 'A':
            count_A += 1
        elif ch == 'B':
            count_B += 1
        elif ch == 'C':
            count_C += 1
        
        diff = max(count_A, count_B, count_C) - min(count_A, count_B, count_C)
        ans = max(ans, diff)
        
    print(ans)

if __name__ == "__main__":
    main()