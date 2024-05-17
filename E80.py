# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         j = 1
#         for i in range(len(nums) - 1, 0, -1):
#             if nums[i - 1] == nums[i]:
#                 j += 1
#             else:
#                 j = 1
#
#             if j > 2:
#                 nums.remove(nums[i])
#                 j += -1
#
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if j == 1 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    res = Solution()
    ret = res.removeDuplicates(nums)
