class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = 0
        no_steps = 0
        end_pos = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                no_steps += 1
                break
            if i == end_pos:
                end_pos = farthest
                no_steps += 1
        return no_steps





if __name__ == "__main__":
    nums = [2,3,1]
    res = Solution()
    ret = res.jump(nums=nums)