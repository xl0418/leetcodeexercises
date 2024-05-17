class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        rows = [[] for i in range(numRows)]
        idx = 0
        d = 1
        if numRows == 1 or numRows >= len(s):
            return s

        for i in range(len_s):
            rows[idx].append(s[i])
            if idx == 0:
                d = 1
            elif idx == numRows -1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)







s = "AB"
numRows = 1
solution = Solution()
solution.convert(s, numRows)