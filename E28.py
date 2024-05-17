class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1

        for i in range(len(haystack) - len(needle) + 1):
            do = []
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    do.append(True)
                else:
                    do.append(False)
                    break

            if all(do):
                return i
        return -1


haystack = "abc"
needle = "c"

solution = Solution()
solution.strStr(haystack, needle)