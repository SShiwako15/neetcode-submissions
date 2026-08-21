class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in nums:
            #check if starting point
            if i - 1 not in numSet:
                count = 0
                #check if consecutive
                while i + count in numSet:
                    count += 1
                longest = max(count, longest)
        return longest
