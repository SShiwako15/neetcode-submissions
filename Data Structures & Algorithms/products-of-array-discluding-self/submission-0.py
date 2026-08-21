class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        mul = 1
        for i in range(len(nums)):
            pre[i] = mul
            mul = nums[i] * mul
        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = mul
            mul = nums[i] * mul
        out = [0] * n
        for i in range(len(nums)):
            out[i] = pre[i] * suf[i]
        return out