class Solution:
    def canJump(self, nums: list[int]) -> bool:
        indices = []
        for idx, value in enumerate(nums):
            if value == 0:
                indices.append(idx)

        if len(indices) == 0:
            return True
        elif len(indices) == len(nums):
            return True
        else:
            bool_v = [False for i in range(len(indices))]
            count = 0
            for zero_id in indices:
                for moveid in range(zero_id):
                    if nums[moveid] > zero_id - moveid:
                        bool_v[count] = True
                        break
                    elif nums[moveid] + moveid + 1 == len(nums):
                        bool_v[count] = True
                        break
                    else:
                        pass
                count += 1

            return all(bool_v)


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    res = Solution()
    ret = res.canJump(nums = nums)

