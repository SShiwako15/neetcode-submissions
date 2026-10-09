class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, val in enumerate(nums):
            missing ^= val ^ i
        return missing