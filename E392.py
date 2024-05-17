class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        count = 0
        for i in range(len_s):
            ls = s[i]
            for j in range(len(t)):
                if t[j] == ls:
                    count += 1
                    t = t[j+1:]
                    break


        return True if count == len_s else False




s = "axc"
t = "ahbgdc"
solution = Solution()
solution.isSubsequence(s, t)