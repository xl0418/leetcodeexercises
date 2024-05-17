class Solution:
    def candy(self, ratings):
        candyarrange = [1 for x in range(len(ratings))]

        for i in range(len(ratings) -1):
            if ratings[i+1]> ratings[i]:
                candyarrange[i+1] = candyarrange[i] + 1

        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                if candyarrange[i-1] > candyarrange[i]:
                    continue
                candyarrange[i-1] = candyarrange[i] + 1

        return sum(candyarrange)


ratings = [1,2,87,87,87,2,1]
candydis = Solution()
candydis.candy(ratings)

