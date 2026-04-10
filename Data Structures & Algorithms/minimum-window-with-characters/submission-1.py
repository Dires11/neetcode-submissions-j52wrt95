class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        current = defaultdict(int)
        need = len(target)
        have = 0
        left, right = 0, 0
        best = s
        found = False
        while right < len(s):
            if s[right] in target:
                current[s[right]] += 1
                if current[s[right]] == target[s[right]]:
                    have += 1
            if have == need:
                found = True
                while left <= right:
                    if s[left] in target:
                        if current[s[left]] == target[s[left]]:
                            if right-left+1 < len(best):
                                best = s[left:right+1]
                            break
                        current[s[left]] -= 1
                    left += 1
            right += 1
        return best if found else ''
        