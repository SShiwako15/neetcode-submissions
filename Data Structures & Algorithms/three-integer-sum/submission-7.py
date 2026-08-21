class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for idx, item in enumerate(nums):
            if item > 0:
                break
            if idx > 0 and item == nums[idx - 1]:
                continue
            fr = idx + 1
            bk = len(nums) - 1
            while fr < bk:
                s = nums[fr] + nums[bk] + item
                if s > 0:
                    bk -= 1
                elif s < 0:
                    fr += 1
                else:
                    out.append([item, nums[fr], nums[bk]])
                    bk -= 1
                    fr += 1
                    while nums[fr] == nums[fr - 1] and fr < bk:
                        fr += 1
        return out
