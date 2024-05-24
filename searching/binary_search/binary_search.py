def binary_search_iterative(elements: list[int], key: int) -> int:
    if not elements:
        return -1
    left: int = 0
    right: int = len(elements)

    while left <= right:
        mid: int = left + (right - left) // 2

        if elements[mid] == key:
            return mid

        if key > elements[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    input: list[int] = [4, 10, 9, 0, 3, 11, 5, 8, 5, 3, 5, 7, 8, 12, 2]
    input.sort()
    key: int = 12

    print(f"{input = }")

    print(f"{key = }")
    print(f"{binary_search_iterative(input, key) = }")

    key: int = 0
    print(f"{key = }")
    print(f"{binary_search_iterative(input, key) = }")

    key: int = 8
    print(f"{key = }")
    print(f"{binary_search_iterative(input, key) = }")
