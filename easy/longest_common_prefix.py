from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        prefix_index = [i + 1 for i in range(len(s))
                        if all(k.startswith(s[:i + 1]) for k in strs)]
        return s[:max([0] + prefix_index)]
