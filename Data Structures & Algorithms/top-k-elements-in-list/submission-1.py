class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = [[] for i in range(len(nums) + 1)]
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i, j in count.items():
            freq_arr[j].append(i)
        out = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:

                out.append(num)
            if len(out) == k:
                return out