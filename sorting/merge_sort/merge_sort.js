function merge_sort(elements) {
    merge_sort_recursive(elements, 0, elements.length)
    return elements;
}

function merge_sort_recursive(elements, start, end) {
    if (start >= end - 1) return;

    var middle = (start + (end - start) / 2) >> 0;
    merge_sort_recursive(elements, start, middle);
    merge_sort_recursive(elements, middle, end);
    merge(elements, start, middle, end);
}

function merge(elements, start, middle, end){
    leftArray = elements.slice(start, middle);
    rightArray = elements.slice(middle, end);
    
    leftSize = leftArray.length;
    rightSize = rightArray.length;
    
    left_i = 0;
    right_i = 0;
    merged_i = start;

    while (left_i < leftSize && right_i < rightSize) {
        if (leftArray[left_i] < rightArray[right_i]) {
            elements[merged_i] = leftArray[left_i];
            left_i++;
        }
        else{
            elements[merged_i] = rightArray[right_i];
            right_i++;
        }
        merged_i++;
    }

    while (left_i < leftSize) {
        elements[merged_i] = leftArray[left_i];
        left_i ++;
        merged_i ++;
    }

    while (right_i < rightSize) {
        elements[merged_i] = rightArray[right_i];
        right_i ++;
        merged_i ++;
    }
}

const input = [3, 7, 2, 9, 0, 6]

console.log(input);
console.log(`merge_sort: ${merge_sort(input.slice())}`);


// console.log(2 + (5-2) / 2);
// console.log((2 + (5-2) / 2 >>0));
// console.log(~~(2 + (5-2) / 2));
// console.log((2 + (5-2) / 2) | 0);