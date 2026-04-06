class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for lt in s:
            if lt not in count: 
                count[lt] = 0
            count[lt] += 1
        print(count)
        for lt in t:
            if lt not in count: 
                return False
            if count[lt] == 0:
                return False
            count[lt] -= 1
        return sum(count.values()) == 0