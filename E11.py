class Solution:
    def maxArea(self, height: list[int]) -> int:
        areas = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                temp_area = (j - i) * min(height[i], height[j])
                areas = max(areas, temp_area)
        return areas





height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
solution.maxArea(height)
