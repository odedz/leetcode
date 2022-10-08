from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i < j:
            if sorted_nums[i][1] + sorted_nums[j][1] > target:
                j -= 1
            elif sorted_nums[i][1] + sorted_nums[j][1] < target:
                i += 1
            else:
                return [sorted_nums[i][0], sorted_nums[j][0]]
