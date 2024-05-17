class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_dic = {}

        m_dic = {}

        for l in ransomNote:
            if l in r_dic:
                r_dic[l] += 1
            else:
                r_dic[l] = 1

        for m in magazine:
            if m in m_dic:
                m_dic[m] += 1
            else:
                m_dic[m] = 1

        for key in r_dic:
            try:
                if r_dic[key] > m_dic[key]:
                    return False
            except:
                return False

        return True




ransomNote = "aa"
magazine = "ab"
solution = Solution()
solution.canConstruct(ransomNote, magazine)


