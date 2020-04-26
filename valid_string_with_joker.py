# https://leetcode.com/problems/valid-parenthesis-string/
def checkValidString(self, s: str) -> bool:
    mmax = mmin = 0
    for i in s:
        mmin +=1 if i == '(' else -1
        mmax +=1 if i != ')' else -1
        if mmax <0:
            break
        mmin = max(mmin, 0)
            
    return mmin == 0