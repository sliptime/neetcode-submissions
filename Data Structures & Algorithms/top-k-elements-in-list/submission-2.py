class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        return heapq.nlargest(k, countMap, key=countMap.get)