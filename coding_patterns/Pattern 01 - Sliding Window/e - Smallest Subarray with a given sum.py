# https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        print(f"target: {target} nums: {nums}")
        min_length = float('inf')
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            count += 1
            if sum >= target:
                print(f"i:{i} sum: {sum} count: {count}")
                while sum >= target:
                    sum -= nums[i-count+1]
                    min_length = min(min_length, count)
                    count -= 1

        if min_length == float('-inf'):
            return 0
        return int(min_length)

    def semiBruteForce(self, target: int, nums: list[int]) -> int:
        """nested for loop with sliding window for k elements. Does not pass"""
        print(f"target: {target} nums: {nums}")
        sum = 0
        sub_array_length = 0
        l = len(nums)
        for i in range(l):
            sum = get_sum(nums, 0, i)
            print(f"i:{i}:{nums[i]} sum: {sum}")
            if sum >= target:
                return i+1
            for j in range(i, l-1):
                sum -= nums[j-1]
                sum += nums[j+1]
                print(
                    f"i:{i}:{nums[i]} j:{j}:{nums[j-1]}-{nums[j+1]} sum: {sum}")
                if sum >= target:
                    return i+1

        return sub_array_length


def get_sum(arr: list, start, end) -> int:
    sum = 0
    for index in range(start, end+1):
        sum += arr[index]
    print(f"\t sum: {sum} - {end} - {start} = {end-start}")
    return sum


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 1, 2, 4, 3]
    target = 15
    # print(solution.minSubArrayLen(target, nums))
    # print(solution.minSubArrayLen(11, [1, 2, 3, 4, 5]))
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
