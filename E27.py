class Solution:
    def removeElement(self, nums, val):
        done = True
        while done:
            try:
                nums.remove(val)
            except:
                done = False
            else:
                done = True
        return len(nums)




nums = [3,2,2,3]
removenumes = Solution()
removenumes.removeElement(nums,3)