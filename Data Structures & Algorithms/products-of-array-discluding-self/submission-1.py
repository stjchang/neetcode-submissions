class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use diviision? 

        prefix, suffix = [1] * len(nums), [1] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        output = [1] * len(nums)

        for i in range(len(nums)):
            pre = prefix[i - 1] if i > 0 else 1
            suf = suffix[i + 1] if i < len(nums) - 1 else 1
            output[i] = pre * suf

        return output
