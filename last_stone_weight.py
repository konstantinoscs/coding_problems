#https://leetcode.com/problems/last-stone-weight/
def lastStoneWeight(self, stones: List[int]) -> int:
    h = []
    fst = snd = 0
    if len(stones) == 1:
        return stones[0]
        
    for i in stones:
        heappush(h, -i)
        
    while len(h):
        fst = -heappop(h)
        if not len(h):
            return fst
        else:
            snd = heappop(h)
        res = fst+snd
        if res != 0:
            heappush(h, -res)
        
    return 0