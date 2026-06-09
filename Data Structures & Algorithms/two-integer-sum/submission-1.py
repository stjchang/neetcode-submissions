class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have to use hashset, two pointer approach doesn't account for negative numbers.
        ogMap = {} # val  -> index

        for i, n in enumerate(nums):
            diff = target-n
            if diff in ogMap:
                return [ogMap[diff], i]
            ogMap[n] = i
            
        