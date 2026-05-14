class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        out = 0

        for num in nums:
            if num-1 not in nums_set:
                curr_length = 0
                while num+curr_length in nums_set: 
                    curr_length += 1
                out = max(curr_length, out)

        return out