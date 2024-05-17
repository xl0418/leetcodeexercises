class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])

        return maxLength






s = "pwwkew"
solution = Solution()
solution.lengthOfLongestSubstring(s)



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        min_len = []
        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                    if j == len(s) - 1:
                        min_len.append(len(substring))
                else:
                    min_len.append(len(substring))
                    break

        return max(min_len) if len(min_len) >1 else min_len[0]

