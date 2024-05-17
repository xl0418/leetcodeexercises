class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            print(i)
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
        return len(nums)




if __name__ == "__main__":
    nums = [1,1,2]
    res = Solution()
    ret = res.removeDuplicates(nums)

