class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r =  0, len(nums) - 1      
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        lower = l
        def bin_ser(l: int, r:  int) -> int:
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1 
            return -1
        out = bin_ser(0, l)
        if out != -1:
            return out
        return bin_ser(l, len(nums) - 1)
