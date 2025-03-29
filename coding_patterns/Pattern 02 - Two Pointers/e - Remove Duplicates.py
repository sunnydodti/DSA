def removeDuplicates(arr: list[int]) -> list[int]:
    replace_index = 1
    for i in range(1, len(arr)):
        print(f"{i=}, {replace_index=}")
        print(f" i:{arr[i]}, i-1:{arr[i-1]}, r:{arr[replace_index]}")
        if (arr[i] != arr[i-1]):
            print(f"swapping {arr[i]} and {arr[replace_index]}")
            arr[replace_index] = arr[i]
            replace_index += 1
        print(f"{arr=}")
    return arr


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count: int = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
        return count

if __name__ == '__main__':
    print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
