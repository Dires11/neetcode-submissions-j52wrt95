class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_i = sorted(range(len(position)), key=lambda i: position[i])
        fleet = 1
        prev = sorted_i.pop() 
        target_t = (target - position[prev]) / speed[prev]
        while sorted_i:
            cur = sorted_i.pop()
            if speed[cur] <= speed[prev]:
                prev = cur
                target_t = (target-position[prev]) / speed[prev]
                fleet += 1
            else: 
                meet_t = (position[prev]-position[cur])/(speed[cur]-speed[prev])
                if meet_t > target_t:
                    prev = cur
                    target_t = (target-position[prev]) / speed[prev]
                    fleet += 1
        return fleet


      