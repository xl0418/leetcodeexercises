class Solution(object):
    def validMountainArray(self, A):
        if len(A) >2:
            count = []
            for i in range(len(A)-1):
                if A[i+1]>A[i]:
                    count.append(0)
                elif A[i+1]<A[i]:
                    count.append(1)
                else:
                    return False
            if count == sorted(count) and sum(count)>0 and sum(count)<len(A)-1:
                return True
            else:
                return False
        else:
            return False


Atest = [1,2,1,5,6,7,3,2,1]
mountain = Solution()
mountain.validMountainArray(A = Atest)