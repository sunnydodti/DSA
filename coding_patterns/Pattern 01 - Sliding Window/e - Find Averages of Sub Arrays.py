def findAvgOfSubarrays(arr: list[int], k: int):
    sum: int = 0
    avg = 0.0
    for i in range(0, k):
        sum += arr[i]
    avg = sum/k
    for i in range(k, len(arr)-1):
        sum += arr[i]
        sum -= arr[i-k]
        avg = max(avg, sum/k)
    return avg


if __name__ == '__main__':
    # print(findAvgOfSubarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
    print(findAvgOfSubarrays([1, 12, -5, -6, 50, 3], 4))
