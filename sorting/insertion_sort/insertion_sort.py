def insertion_sort(elements: list[int]) -> list[int]:
    for i in range(1, len(elements)):
        j: int = i-1
        current: int = elements[i]

        while j >= 0 and current < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j + 1] = current

    return elements


if __name__ == '__main__':
    input: list[int] = [8, 2, 2, 9, 1]
    print(input)
    print(f"{insertion_sort(input[:]) = }")
