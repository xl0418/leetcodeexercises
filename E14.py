class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""

        first_word = strs[0]
        for l in range(len(first_word)):
            dos = []
            for i in range(1, len(strs)):
                if len(strs[i]) > l:
                    if first_word[l] == strs[i][l]:
                        dos.append(True)
                    else:
                        dos.append(False)
                        break
                else:
                    dos.append(False)

            if all(dos):
                ans+=first_word[l]
            else:
                break

        return ans




strs = ["ab", "a"]
solution = Solution()
solution.longestCommonPrefix(strs)
