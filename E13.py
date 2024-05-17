class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        if 'CM' in s:
            s = s.replace('CM', '')
            output += 900

        if 'CD' in s:
            s = s.replace('CD', '')
            output += 400

        if 'XC' in s:
            s = s.replace('XC', '')
            output += 90

        if 'XL' in s:
            s = s.replace('XL', '')
            output += 40

        if 'IX' in s:
            s = s.replace('IX', '')
            output += 9

        if 'IV' in s:
            s = s.replace('IV', '')
            output += 4


        for i in range(len(s)):
            if s[i] == "M":
                output += 1000
            elif s[i] == "D":
                output += 500
            elif s[i] == "C":
                output += 100
            elif s[i] == "L":
                output += 50
            elif s[i] == "X":
                output += 10
            elif s[i] == "V":
                output += 5
            elif s[i] == "I":
                output += 1
            else:
                return None
        return output




s = "MCMXCIV"
solution = Solution()
solution.romanToInt(s)