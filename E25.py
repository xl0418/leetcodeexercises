class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_s = len(s)
        if len_s <2:
            return True
        else:
            letter_vec = []
            for i in range(len_s):
                if s[i].isalnum():
                    letter_vec.append((s[i].lower()))

            for j in range(len(letter_vec) // 2):
                if letter_vec[j] != letter_vec[len(letter_vec) - 1 - j]:
                    return False

            return True






s = "A man, a plan, a canal: Panama"
solution = Solution()
solution.isPalindrome(s)