function totalFruit(fruits: number[]): number {
    let start: number = 0;
    let max_length: number = 0;
    let map: Record<number, number> = {};

    for (let i: number = 0; i < fruits.length; i++) {
        if (Object.keys(map).length < 2) {
            map[fruits[i]] = 0;
        }
        map[fruits[i]]++;

        while (Object.keys(map).length > 2) {
            map[fruits[start]]--;
            if (map[fruits[start]] === 0) {
                delete map[fruits[start]];
            }
            start++;
        }
        max_length = Math.max(max_length, i - start + 1);
    }
    return max_length;

};

console.log(totalFruit([1, 2, 1]));