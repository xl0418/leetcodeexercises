class Solution:
    def hIndex(self, citations: list[int]) -> int:

        sorted_cit = sorted(citations)
        len_cit = len(citations)
        if sorted_cit[0] > len_cit:
                return len_cit
        else:
            hind = 0
            for i in range(len(sorted_cit)):
                if len_cit - i >= sorted_cit[i]:
                    hind = sorted_cit[i]
                else:
                    hind_type2 = min(sorted_cit[i], len_cit - i)
                    hind = max(hind, hind_type2)
                    break
            return hind




if __name__ == "__main__":
    citations = [3,0,6,1,5]
    res = Solution()
    ret = res.hIndex(citations)



class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        max_index = len(citations)
        for i in citations:
            if i<max_index:
                max_index-=1
        return max_index