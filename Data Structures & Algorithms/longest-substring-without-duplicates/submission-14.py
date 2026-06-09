class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        unique = set()
        left = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            count = max(count, right - left + 1)
        
        return count
        
            