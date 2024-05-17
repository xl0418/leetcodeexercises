class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if start > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif end <newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]

        ans.append(newInterval)
        return ans





intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

solution = Solution()
solution.insert(intervals, newInterval)
