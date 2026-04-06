class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [sorted_counts[i][0] for i in range(k)]