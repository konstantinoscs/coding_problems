# https://leetcode.com/problems/number-complement/
def findComplement(self, num: int) -> int:
    res = []
    while num:
        if num&1:
            res.append("0")
        else:
            res.append("1")
        num>>=1
    return int("".join(res[::-1]), 2)