class Solution:   
    def bin_search(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        if nums[m] > target:
            return self.bin_search(nums, target, l, m - 1)
        else:
            return self.bin_search(nums, target, m + 1, r)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, target, 0, len(nums) - 1)