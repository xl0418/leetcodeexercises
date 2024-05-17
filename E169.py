class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        threshold = len(nums) // 2
        if threshold == 0:
            return nums[0]
        sorted_nums = sorted(nums)
        j = 1
        for i in range(len(nums) - 1):
            if sorted_nums[i+1] == sorted_nums[i]:
                j += 1
            else:
                j = 1
            if j > threshold:
                output = sorted_nums[i]
                break
        return output

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

if __name__ == "__main__":
    nums = [1]
    solution = Solution()
    solution.majorityElement(nums)
