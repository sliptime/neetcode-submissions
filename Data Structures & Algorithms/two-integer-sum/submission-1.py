class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            if target - nums[i] in hashset:
                return [hashset.get(target - nums[i]),i]
            hashset[nums[i]] = i

        return [0,0]