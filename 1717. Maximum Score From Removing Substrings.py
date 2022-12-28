class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x>y:
            target1 = "ab"
            target2 = "ba"
        else:
            target1 = "ba"
            target2 = "ab"

        score = 0
        score1 = max(x, y)
        score2 = min(x, y)
        do = True
        while do:
            if target1 in s:
                pos = s.index(target1)
                s = s[:pos] + s[(pos+2):]
                score += score1
            elif target2 in s:
                pos = s.index(target2)
                s = s[:pos] + s[(pos+2):]
                score += score2
            else:
                do = False

        return score


if __name__ == "__main__":
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    res = Solution()
    ret = res.maximumGain(s=s, x=x, y=y)