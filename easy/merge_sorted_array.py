from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[n:] = nums1[:m]
        i, j, k = n, 0, 0
        while i < m + n and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        if i < m + n:
            nums1[k:] = nums1[i:]
        else:
            nums1[k:] = nums2[j:]
