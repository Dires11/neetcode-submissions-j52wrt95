class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_i = sorted(range(len(position)), key=lambda i: position[i])
        slowest_time = 0
        fleet = 0
        while sorted_i:
            i = sorted_i.pop()
            time = (target-position[i]) / speed[i]
            if time > slowest_time:
                fleet += 1
                slowest_time = time
        return fleet
      