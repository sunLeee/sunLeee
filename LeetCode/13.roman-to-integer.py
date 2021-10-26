#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        syms = {"M":1000, "D":500, "C":100, "L": 50, "X":10, "V":5, "I":1}
        rst, prev = 0, 0
        for str_idx in s[::-1] :
            if syms[str_idx] >= prev :
                rst += syms[str_idx]
            else :
                rst -= syms[str_idx]
            prev = syms[str_idx]
        return rst
# @lc code=end

