class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            words = s.split(' ')
            words_len = []
            for word in words:
                if len(word) > 0:
                    words_len.append(len(word))
            return words_len[-1]


s = "   fly me   to   the moon  "
solution = Solution()
solution.lengthOfLastWord(s)
