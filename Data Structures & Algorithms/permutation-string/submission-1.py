class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = Counter(s1)
        window_len = len(s1)
        for l in range(len(s2)-window_len+1):
            if target_count == Counter(s2[l:l+window_len]):
                return True
        return False