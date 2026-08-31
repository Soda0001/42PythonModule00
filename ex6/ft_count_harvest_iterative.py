def ft_count_harvest_iterative():
    total_day = int(input("Days until harvest: "))
    current_day = 1
    for i in range(1, total_day + 1):
        print(f"Day {current_day}")
        if (current_day == total_day):
            print("Harvest time!")
        current_day += 1
        