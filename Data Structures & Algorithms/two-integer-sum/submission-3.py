class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have to use hashset, two pointer approach doesn't account for negative numbers.
        hmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i]
            hmap[n] = i
