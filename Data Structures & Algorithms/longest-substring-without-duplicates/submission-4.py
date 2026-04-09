class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen = {}
        i = 0
        out = 0
        for j in range(len(s)):
            if s[j] in seen:
                i = max(i, seen[s[j]]+1) 
            seen[s[j]] = j
            out = max(out, j-i+1)
        return out
