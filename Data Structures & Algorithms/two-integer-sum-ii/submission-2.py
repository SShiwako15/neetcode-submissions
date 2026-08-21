class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for idx, i in enumerate(numbers):
            need = target - i
            if need in hm:
                return [hm[need] + 1, idx + 1]
            hm[i] = idx