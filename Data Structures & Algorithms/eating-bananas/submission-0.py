class Solution:
     def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mini = 0
        while l <= r:
            mid = l + (r - l) // 2
            total = 0
            for i in piles:
                total += -(-i // mid)
            if total <= h:
                mini = mid
                r = mid - 1
            else:
                l = mid + 1
        return mini