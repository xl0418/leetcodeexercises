class Solution:
    def arrayNesting(self, nums):
        afterlist = [nums[0]]
        for i in range(1,len(nums)):
            afterlist.append(nums[afterlist[i-1]])


nums = [5,4,0,3,1,6,2]
an = Solution()
an.arrayNesting(nums)