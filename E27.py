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
val = 3

removenumes = Solution()
removenumes.removeElement(nums,3)


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 100
            else:
                k += 1
        nums.sort()
        return k