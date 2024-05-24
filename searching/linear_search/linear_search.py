def linear_search(input: list[int], key: int) -> int:

    for i in range(len(input)):
        if input[i] == key:
            return i

    return -1


def linear_search_v2(input: list[int], key: int) -> int:
    count: int = 0
    for num in input:
        if num == key:
            return count
        count += 1

    return -1


if __name__ == "__main__":
    input: list[int] = [8, 11, 3, 94, 0, 32, 5, 7, 9, 1999, 38, 94]
    key: int = 38
    print(f"{input = }")
    print(f"{key = }")
    print(f"{linear_search(input, key) = }")
    print(f"{linear_search_v2(input, key) = }")
