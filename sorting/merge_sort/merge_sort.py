def merge_sort(elements: list[int]) -> list[int]:

    merge_sort_recursive(elements, 0, len(elements))

    return elements


def merge_sort_recursive(elements: list[int], start: int, end: int) -> list[int]:
    if start >= end - 1:
        return
    middle: int = start + (end - start) // 2
    merge_sort_recursive(elements, start, middle)
    merge_sort_recursive(elements, middle, end)

    merge(elements, start, middle, end)

def merge(elements: list[int], start: int, middle: int, end: int) -> None:
    left_array: list[int] = elements[start:middle]
    right_array: list[int] = elements[middle:end]

    left_size: int = len(left_array)
    right_size: int = len(right_array)

    left_i: int = 0
    right_i: int = 0
    merged_i: int = start

    while left_i < left_size and right_i < right_size:
        if left_array[left_i] < right_array[right_i]:
            elements[merged_i] = left_array[left_i]
            left_i += 1
        else:
            elements[merged_i] = right_array[right_i]
            right_i += 1

        merged_i += 1

    while left_i < left_size:
        elements[merged_i] = left_array[left_i]
        left_i += 1
        merged_i += 1

    while right_i < right_size:
        elements[merged_i] = right_array[right_i]
        right_i += 1
        merged_i += 1


if __name__ == '__main__':
    input: list[int] = [8, 2, 2, 9, 1]
    print(input)
    print(f"{merge_sort(input[:]) = }")
