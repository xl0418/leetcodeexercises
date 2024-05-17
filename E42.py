class Solution:
    def trap(self, height: list[int]) -> int:
        left = [0]
        right = []
        for i in range(1, len(height)):
            left.append(max(height[:i]))

        for i in range(len(height) - 1):
            right.append(max(height[i:]))
        right.append(0)

        fill = 0
        for i in range(len(height)):
            if height[i] < min(left[i], right[i]):
                fill += min(left[i], right[i]) - height[i]

        return fill



height = [4,2,0,3,2,5]
solution = Solution()
solution.trap(height)



