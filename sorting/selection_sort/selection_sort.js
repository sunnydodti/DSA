function selection_sort(elements) {
    var length = elements.length;

    for (let i = 0; i < length - 1; i++) {
        var min_element_index = i;

        for (let j = i + 1; j < length; j++) {
            if (elements[j] < elements[min_element_index]) {
                min_element_index = j;
            }
        }

        [elements[min_element_index], elements[i]] = [elements[i], elements[min_element_index]]
    }
    return elements;
}

const input = [3, 7, 2, 9, 0, 6]

console.log(`selection_sort: ${selection_sort(input.slice())}`);
