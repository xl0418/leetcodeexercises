class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            sorted_nums = sorted(nums)
            consecutive_len = 1
            consecutive_len_list = [1]
            for i in range(len(nums) - 1):
                if sorted_nums[i + 1] - sorted_nums[i] == 1:
                    consecutive_len += 1
                    if i + 1 == len(nums) - 1:
                        consecutive_len_list.append(consecutive_len)
                elif sorted_nums[i + 1] - sorted_nums[i] == 0:
                    consecutive_len_list.append(consecutive_len)
                else:
                    consecutive_len_list.append(consecutive_len)
                    consecutive_len = 1

            return max(consecutive_len_list)



if __name__ == "__main__":
    nums = [0,0,-1]
    solution = Solution()
    ot = solution.longestConsecutive(nums)
