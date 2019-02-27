class Solution(object):
    def diStringMatch(self, S):
        i = range(len(S)+1)
        output = []
        for letter in S:
            if letter == 'I':
                output.append(min(i))
                i = i[1:]
            else:
                output.append(max(i))
                i = i[:-1]
        output.append(i[0])
        return output
Stest = 'IIDDDII'
dis = Solution()
dis.diStringMatch(S=Stest)