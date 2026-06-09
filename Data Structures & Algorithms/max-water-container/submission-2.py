class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights) - 1
        while l is not r:
            maximum = max(maximum, min(heights[l], heights[r]) * (r - l)) # volume calculation
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maximum