def totalFruit(fruits: list[int]) -> int:
    start: int  = 0
    max_length = 0
    map: dict[int, int] = {}
    
    for i in range(len(fruits)):
        if fruits[i] not in map:
            map[fruits[i]] = 0
        map[fruits[i]] += 1
        
        if len(map) > 2:
            map[fruits[start]] -= 1
            
            if map[fruits[start]] == 0:
                del map[fruits[start]]
            start += 1
        max_length = max(max_length, i - start + 1)
    return max_length
if __name__ == '__main__':
    print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))