class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        len_nums = len(nums)
        if len_nums < 2:
            return []

        for i in range(len_nums - 1):
            otherp = target - nums[i]
            if otherp in nums[(i+1):]:
                for j in range(i+1, len_nums):
                    if nums[j] == otherp:
                        return [i, j]
            else:
                continue

        return []




nums = [2, 7, 11, 15]
target = 9
solution = Solution()
solution.twoSum(nums, target)