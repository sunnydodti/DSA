def selection_sort(elements: list[int]) -> list[int]:
    for i in range(len(elements)):
        min_element_index: int = i

        for j in range(i, len(elements)):
            if elements[j] < elements[min_element_index]:
                min_element_index = j

        elements[i], elements[min_element_index] = elements[min_element_index], elements[i]

    return elements


def selection_sort_optimized(elements: list[int]) -> list[int]:
    length: int = len(elements)
    min_element_index: int = -1
    for i in range(length - 1):
        min_element_index = i

        for j in range(i + 1, length):
            if elements[j] < elements[min_element_index]:
                min_element_index = j

        elements[i], elements[min_element_index] = elements[min_element_index], elements[i]

    return elements


if __name__ == '__main__':
    input: list[int] = [8, 2, 2, 9, 1, 100, 0]
    print(input)
    print(f"{selection_sort(input[:]) = }")
    print(f"{selection_sort_optimized(input[:]) = }")
