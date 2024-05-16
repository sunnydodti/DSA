function insertion_sort(elements) {
    for (let i = 1; i < elements.length; i++) {
        const current = elements[i];
        let j = i - 1;

        while (j >= 0 && current < elements[j]) {
            elements[j + 1] = elements[j];
            j--;
        }

        elements[j + 1] = current;
    }
    return elements;
}

const input = [3, 7, 2, 9, 0, 6]

console.log(`insertion_sort: ${insertion_sort(input.slice())}`);
