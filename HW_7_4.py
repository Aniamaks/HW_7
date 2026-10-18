def common_elements():
    first = [num for num in range(100) if num % 3 == 0]
    second = [num for num in range(100) if num % 5 == 0]

    return set(first) & set(second)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}