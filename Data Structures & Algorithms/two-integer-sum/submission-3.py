class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i, val in enumerate(nums):
            target_val = target - val
            if target_val in hashset:
                return [hashset[target_val],i]
            hashset[val] = i