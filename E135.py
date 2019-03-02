class Solution:
    def candy(self, ratings):
        candyarrange = [1]
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i]:
                candyarrange.append(candyarrange[i]+1)
            else:
                candyarrange.append(candyarrange[i]-1)
        return sum([candyarrange[i]-min(candyarrange)+1 for i in range(len(candyarrange))])



ratings = [1,3,2,2,1]
candydis = Solution()
candydis.candy(ratings)

