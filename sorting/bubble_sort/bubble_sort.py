def bubble_sort(elements: list[int]) -> list[int]:

    for _ in range(len(elements)):
        for j in range(len(elements) - 1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

    return elements


def bubble_sort_optimized(elements: list[int]) -> list[int]:
    length: int = len(elements)

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

    return elements


if __name__ == '__main__':
    input = [8, 2, 2, 9, 1]
    print(input)
    print(f"{bubble_sort(input[:]) = }")
    print(f"{bubble_sort_optimized(input[:]) = }")
