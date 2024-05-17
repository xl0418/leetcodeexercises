class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[(i + 1):min(i+1+k, len(nums))]:
                return True

        return False




nums = [1,2,3,1,2,3]
k = 2
solution = Solution()
solution.containsNearbyDuplicate(nums, k)


