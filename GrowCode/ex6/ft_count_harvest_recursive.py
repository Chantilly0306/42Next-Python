def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count_up(current: int) -> None:
        if current > days:
            return
        print(f"Day {current}")
        count_up(current + 1)

    count_up(1)
    print("Harvest time!")
