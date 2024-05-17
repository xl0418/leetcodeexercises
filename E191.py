import numpy as np
class Solution:
    def hammingWeight(self, n: int) -> int:
        do = True
        exp_idx = []

        while do:
            x = np.floor(np.log2(n))
            n = n - 2 ** x
            if n == 0:
                exp_idx.append(x)
                do = False
            else:
                if x == 0:
                    if n == 1:
                        exp_idx.append(1)
                    do = False
                else:
                    exp_idx.append(x)


        return len(exp_idx)







n = 11
solution = Solution()
solution.hammingWeight(n)