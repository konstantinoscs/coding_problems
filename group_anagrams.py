# https://leetcode.com/problems/group-anagrams/
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    strMap = {}
    for s in strs:
        sorteds = ''.join(sorted(s))
        if sorteds in strMap.keys():
            strMap[sorteds].append(s)
        else:
            strMap[sorteds] = [s]
    return list(strMap.values())