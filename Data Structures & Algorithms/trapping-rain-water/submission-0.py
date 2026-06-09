class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        count = 0   

        while left < right: 
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                count += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                count += max_right - height[right]
                right -= 1
    
        return count


        