function linear_search(input, ket) {
    for (let i = 0; i < input.length; i++) {
        if( input[i] === key) return i;
    }
    return -1;
}

function linear_search_v2(input, ket) {
    var count = 0;
    for (const num of input) {
        if (num === key) return count;
        count++;
    }
    return -1;
}

const input = [4, 5, 9, 0, 3, 8, 5, 8, 5, 3, 5, 7, 8, 0, 2];
const key = 2;
console.log(`input: ${input}`);
console.log(`key: ${key}`);
console.log(`linear_search: ${linear_search(input, key)}`);
console.log(`linear_search_v2: ${linear_search_v2(input, key)}`);