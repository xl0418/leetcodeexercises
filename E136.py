class Solution(object):
    def singleNumber(self, nums):
        nums_sort = sorted(nums)
        while len(nums_sort)>1:
            if nums_sort[0] == nums_sort[1]:
                nums_sort = nums_sort[2:]
            else:
                return nums_sort[0]
        return nums_sort[0]


nums = [2,2,1]
checksingle = Solution()
checksingle.singleNumber(nums)