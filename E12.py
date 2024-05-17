class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''

        if num >= 1000:
            ans += 'M' * int(num // 1000)
            num = num % 1000

        if num >= 100 and num < 1000:
            if num // 100 == 9:
                ans += 'CM'
            elif num // 100 >=5 and num // 100 <9:
                ans += 'D' + 'C' * int(num // 100 -5)
            elif num // 100 == 4:
                ans += 'CD'
            else:
                ans += 'C' * int(num // 100)

            num = num % 100

        if num >= 10 and num < 100:
            if num // 10 == 9:
                ans += 'XC'
            elif num // 10 >= 5 and num // 10 < 9:
                ans += 'L' + 'X' * int(num // 10 - 5)
            elif num // 10 == 4:
                ans += 'XL'
            else:
                ans += 'X' * int(num // 10)

            num = num % 10

        if num >= 1 and num < 10:
            if num == 9:
                ans += 'IX'
            elif num >= 5 and num < 9:
                ans += 'V' + 'I' * int(num - 5)
            elif num == 4:
                ans += 'IV'
            else:
                ans += 'I' * int(num)


        return ans




num = 58
solution = Solution()
solution.intToRoman(num)