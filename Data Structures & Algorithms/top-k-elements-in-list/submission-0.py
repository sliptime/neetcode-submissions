class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for num in nums:
            if countMap[num] == None:
                countMap[num] = 0
            else:
                countMap[num] += 1
        return heapq.nlargest(k, countMap, key=countMap.get)