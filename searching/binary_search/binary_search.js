function binary_search(elements, key) {
    if (elements.length < 1) return -1;

    left = elements[0];
    right = elements.length - 1


    while (left <= right) {
        mid = (left + (right - left) / 2) >> 0;
        if (key == elements[mid]) return mid;

        if (key < elements[mid]) {
            right = mid - 1;
        }
        else {
            left = mid + 1
        }
    }
    return -1;
}

const input = [3, 7, 2, 9, 0, 6];
input.sort()

key = 2
console.log(input);
console.log(key);
console.log(`binary_search: ${binary_search(input, key)}`);

key = 9
console.log(key);
console.log(`binary_search: ${binary_search(input, key)}`);

key = 92
console.log(key);
console.log(`binary_search: ${binary_search(input, key)}`);