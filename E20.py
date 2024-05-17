
class Solution:
    def isValid(self, s: str) -> bool:
        lefts = []
        rights = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                lefts.append(i)

            if i == ")":
                if len(lefts)>0 and lefts[-1] == "(":
                    lefts.pop()
                else:
                    return False

            if i == "]":
                if len(lefts)>0 and lefts[-1] == "[":
                    lefts.pop()
                else:
                    return False

            if i == "}":
                if len(lefts)>0 and lefts[-1] == "{":
                    lefts.pop()
                else:
                    return False

        return True if len(lefts) == 0 else False






s = "]"
solution = Solution()
solution.isValid(s)