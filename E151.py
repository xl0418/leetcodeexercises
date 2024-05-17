class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return []
        words = s.split(" ")
        rev_words = []
        for i in range(len(words)-1, -1, -1):
            if len(words[i]) > 0:
                rev_words.append(words[i])

        return ' '.join(rev_words)



s = "  hello world  "
solution = Solution()
solution.reverseWords(s)