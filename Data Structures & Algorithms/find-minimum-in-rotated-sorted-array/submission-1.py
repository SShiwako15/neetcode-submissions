class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mini = nums[0]
        while l <= r:
            if nums[l] <= nums[r]:
                mini = min(mini, nums[l])
                break
            mid = l + (r - l) // 2
            mini = min(mini, nums[mid])
            if nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return mini
        
        
