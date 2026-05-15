class Solution:
    def trap(self, height: List[int]) -> int:
        maxWA = 0
        if len(height) > 2:
            i = 1
            j = len(height)-2
            waterLevel = 0
            while i <= j:
                waterLevel = max(waterLevel, min(height[i-1], height[j+1]))
                if height[i-1] < height[j+1]:
                    if waterLevel >= height[i]:
                        maxWA += waterLevel - height[i]
                    i += 1
                else:
                    if waterLevel >= height[j]:
                        maxWA += waterLevel - height[j]
                    j -= 1
        return maxWA