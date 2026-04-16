class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        r = piles[-1]
        l = 1
        while l <= r:
            mid = (l+r)//2
            time = 0
            for i in range(len(piles)-1, -1, -1):
                if mid >= piles[i]:
                    time += i+1
                    break
                else: 
                    time += math.ceil(piles[i]/mid)
            if time <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l