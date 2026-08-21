class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 == l2:
            if Counter(s1) == Counter(s2):
                return True
            else:
                return False

        set1 = Counter(s1)
        set2 = Counter()
        l = 0
        for r in range(l2):
            set2[s2[r]] += 1

            if r - l + 1 > l1:
                set2[s2[l]] -= 1
                if set2[s2[l]] == 0:
                    del set2[s2[l]]
                l += 1
            if set1 == set2:
                return True
        return False