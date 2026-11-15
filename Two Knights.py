def main():
    k = int(input())

    for i in range(1, k + 1): 
        total_placement = i ** 2 * (i ** 2 - 1) // 2
        invalic_placement = 4 * (i - 1) * (i - 2)
        valid_placement = total_placement - invalic_placement
        print(valid_placement)

if __name__ == "__main__":
    main()