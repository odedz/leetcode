"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        close_paran = {'(': ')', '{': '}', '[': ']'}
        paran_stack = []
        for c in s:
            if c in {'(', '{', '['}:
                paran_stack.append(c)
            else:
                if (not paran_stack or
                        close_paran[paran_stack.pop()] != c):
                    return False
        if paran_stack:
            return False
        return True
