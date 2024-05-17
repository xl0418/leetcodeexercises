
from itertools import permutations
import re
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        permutation_words = list(permutations(words, len(words)))
        pos = []
        for i in range(len(permutation_words)):
            t = ''.join(permutation_words[i])
            for j in range(len(s) - len(t) + 1):
                do = True
                while do:
                    if s[j: (j+len(t))] == t:
                        if j not in pos:
                            pos.append(j)
                        break
                    else:
                        j += 1


        return sorted(pos)




s = "barfoothefoobarman"
words = ["foo","bar"]
solution = Solution()
solution.findSubstring(s, words)