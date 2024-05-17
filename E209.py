class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        if sum(nums) < target:
            return 0

        s, l, ans = 0, 0, len(nums)

        for r, val in enumerate(nums):
            s += val  #
            while s >= target:
                s -= nums[l]
                ans = min(ans, r - l + 1)
                l += 1  #

        return ans

target = 80
nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
solution = Solution()
solution.minSubArrayLen(target, nums)




class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0

        ans = 999999
        temp_addup = 0
        j = 0
        i = 0
        start = 0
        while temp_addup < target and i < len(nums):
            temp_addup += nums[i]
            i += 1
            j += 1
            while temp_addup >= target:
                temp_addup -= nums[start]
                if temp_addup >= target:
                    j-= 1
                    start += 1
                else:
                    ans = min(ans, j)
                    temp_addup = 0
                    j = 0
                    i = start + 1
                    start = i


        return ans