def partition(elements: list[int], start: int, end: int) -> int:

    pivot: int = elements[end]
    swap_index: int = start - 1

    for i in range(start, end):
        if elements[i] <= pivot:
            swap_index += 1

            elements[swap_index], elements[i] = elements[i], elements[swap_index]

    swap_index += 1
    elements[swap_index], elements[end] = elements[end], elements[swap_index]

    return swap_index


def quick_sort(elements: list[int], start: int, end: int) -> list[int]:
    if start < end:
        pivot: int = partition(elements, start, end)
        quick_sort(elements, start, pivot - 1)
        quick_sort(elements, pivot + 1, end)
    return elements


if __name__ == "__main__":
    input: list[int] = [4, 9, 9, 0, 3, 4, 5, 8, 5, 3, 5, 7, 8, 6, 2]
    print(f"{input = }")
    print(f"{quick_sort(input[:], 0, len(input) - 1) = }")
