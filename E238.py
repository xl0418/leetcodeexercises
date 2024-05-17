class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        profix = [1] * len_nums
        sufix = [1] * len_nums
        for i in range(1, len(nums)):
            profix[i] = profix[i-1] * nums[i - 1]

        for i in range(len_nums - 2, -1, -1):
            sufix[i] = sufix[i+1] * nums[i+1]

        output = [profix[i] * sufix[i] for i in range(len_nums)]


        return output





if __name__ == "__main__":
    nums = [1,2,3,4]
    res = Solution()
    ret = res.productExceptSelf(nums)

