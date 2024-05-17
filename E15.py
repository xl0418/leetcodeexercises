class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) -1):
            left = i +1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    left += 1
                    if temp not in ans:
                        ans.append(temp)

                elif total < 0:
                    left += 1
                else:
                    right += -1


        return ans



nums = [-1,0,1,2,-1,-4]
solution = Solution()
solution.threeSum(nums)

