function bubble_sort(elements) {
    for (let i = 0; i < elements.length; i++) {
        for (let j = 0; j < elements.length - 1; j++) {
            if (elements[j] > elements[j + 1]) {
                [elements[j], elements[j + 1]] = [elements[j + 1], elements[j]];
            }
        }
    }
    return elements;
}

function bubble_sort_optimized(elements) {
    const length = elements.length;
    for (let i = 0; i < length - 1; i++) {
        for (let j = 0; j < length - 1 - i; j++) {
            if (elements[j] > elements[j + 1]) {
                [elements[j], elements[j + 1]] = [elements[j + 1], elements[j]];
            }
        }
    }
    return elements;
}

const input = [3, 7, 2, 9, 0, 6]

console.log(`bubble_sort: ${bubble_sort(input)}`);
console.log(`bubble_sort_optimized: ${bubble_sort(input)}`);