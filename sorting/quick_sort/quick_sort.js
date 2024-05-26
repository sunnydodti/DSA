function partition(elements, start, end) {

    pivot = elements[end]
    swap_index = start - 1;

    console.log(start, end);
    console.log(elements.slice(start, end));
    for (let i = start; i < end; i++) {
        if (elements[i] < pivot) {
            swap_index += 1;

            [[elements[swap_index], [elements[i]]]] = [[elements[i], [elements[swap_index]]]];
        }
    }
    swap_index += 1;
    [[elements[swap_index], [elements[end]]]] = [[elements[end], [elements[swap_index]]]];
    return swap_index;
}

function quick_sort(elements, start, end) {
    if (start < end) {
        pivot = partition(elements, start, end);
        console.log(`pivot: ${pivot}`);
        quick_sort(elements, start, pivot - 1);
        quick_sort(elements, pivot + 1, end);
    }
    return elements;
}

const input = [3, 7, 2, 9, 0, 6];

console.log(input);
console.log(`quick_sort: ${quick_sort(input.slice(), 0, input.length - 1)}`);