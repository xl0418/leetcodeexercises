class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def addp(left, right, s):
            if len(s) == n * 2:
                ans.append(s)
                return

            if left < n:
                addp(left + 1, right, s + "(")

            if right<left:
                addp(left, right + 1, s + ")")

        ans = []
        addp(0, 0, '')
        return ans



n = 3
solution = Solution()
solution.generateParenthesis(n)
