class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l <= r:
            speed = (r+l)//2
            time = sum(math.ceil(pile/speed) for pile in piles)
            if time > h:
                l = speed+1
            else:
                r = speed-1
        return l
             