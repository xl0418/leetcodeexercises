class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        kk = k % len_nums

        nums_part1 = nums[(len_nums - kk):(len_nums)]
        nums[kk:len_nums] = nums[0:(len_nums - kk)]
        nums[0:kk] = nums_part1

        return

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    solution = Solution()
    solution.rotate(nums, 3)
