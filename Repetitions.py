def main():
    str = input()
    max_len = 0
    current_len = 1
    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    max_len = max(max_len, current_len)
    print(max_len)

if __name__ == "__main__":
    main()