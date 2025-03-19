# def maxSubarrayOfSizeK(k, arr):
#     sum: int = get_sum(arr, 0, k-1)
#     maxSum: int = sum
    
#     for i in range(k, len(arr) - 1):
#         print(f"i:{i}:{arr[i]} - sum: {sum}")
#         sum -= arr[i-k]
#         sum += arr[i]
#         maxSum = max(maxSum, sum)

#     return maxSum

# def get_sum(arr: list, start, end) -> int:
#     sum = 0
#     for index in range(start, end+1):
#         sum += arr[index]
#     print(f"\t sum: {sum} - {end} - {start} = {end-start}")
#     return sum

# if __name__ == '__main__':
#     print(maxSubarrayOfSizeK(3, [2, 1, 5, 1, 3, 2]))
