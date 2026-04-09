class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen = {s[0]: 0}
        i, j = 0, 1
        out = 1
        while i < j and j < len(s):
            if s[j] in seen and seen[s[j]] >= i and seen[s[j]] < j:
                out = max(out, j-i)
                i = seen[s[j]] + 1
            seen[s[j]] = j
            j+=1
        return max(out, j-i)
