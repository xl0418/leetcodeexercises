class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits_val = 0
        for i in range(len(digits)):
            digits_val += digits[i] * 10 ** (len(digits) - 1 - i)

        digits_plutsone = str(digits_val + 1)

        return [int(x) for x in digits_plutsone]



digits = [1,2,3]
solution = Solution()
solution.plusOne(digits)
