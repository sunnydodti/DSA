def removeElement(arr: list[int], key: int) -> int:
    count: int = 0
        
    for i in range(len(arr)):
        if arr[i] != key:   
            arr[count] = arr[i]
            count += 1
            
    return count    

if __name__ == '__main__':
    inp = [2, 11, 2, 2, 1]
    print(inp)
    print(removeElement(inp, 2))
    print(inp)
    
    inp = [3, 2, 3, 6, 3, 10, 9, 3]
    print(inp)
    print(removeElement(inp, 3))
    print(inp)