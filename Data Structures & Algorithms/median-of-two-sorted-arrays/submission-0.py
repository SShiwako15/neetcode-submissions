class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = total // 2
        if m < n:
            A,B = nums1, nums2
        else:
            B,A = nums1, nums2

        l, r = 0, len(A)  - 1
        while True:
            mid = l + (r - l) // 2
            side = half - mid - 2

            Aleft = A[mid] if mid >= 0 else float("-inf")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("inf")
            Bleft = B[side] if side >= 0 else float("-inf")
            Bright = B[side + 1] if side + 1 < len(B) else float("inf")

            if Bleft <= Aright and Aleft <= Bright:
                if total % 2:
                    return min(Aright, Bright)
                return (min(Aright, Bright) + max(Aleft, Bleft))/2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1