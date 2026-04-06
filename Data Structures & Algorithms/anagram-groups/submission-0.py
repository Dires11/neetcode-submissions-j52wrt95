class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counter = {}
            for l in word:
                counter[l] = counter.get(l, 0) + 1
            key = frozenset(counter.items())
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())       