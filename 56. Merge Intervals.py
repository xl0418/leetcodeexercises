import numpy as np
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        len_int = len(intervals)
        sorted_ind = [intervals[i][0] for i in range(len_int)]
        sind = np.argsort(sorted_ind)
        sorted_int = []
        for ii in range(len_int):
            sorted_int.append(intervals[sind[ii]])


        expand = []
        for item in range(len_int):
            expand.append(sorted_int[item][0])
            expand.append(sorted_int[item][1])

        output = []
        while len(expand) > 2:
            if expand[1] >= expand[2]:
                if expand[1] >= expand[3]:
                    expand.pop(2)
                    expand.pop(2)
                else:
                    expand.pop(1)
                    expand.pop(1)
            else:
                output.append([expand[0], expand[1]])
                expand.pop(0)
                expand.pop(0)

        if len(expand) == 2:
            output.append(([expand[0], expand[1]]))

        return output





if __name__ == "__main__":
    intervals = [[1,4],[2,3]]
    res = Solution()
    ret = res.merge(intervals=intervals)