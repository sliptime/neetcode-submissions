class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        con_sets = defaultdict(set)

        for num in nums:
            nums_set.add(num)

        for num in nums:
            if num-1 not in nums_set:
                con_sets[num] = 0

        out = 0
        for num in con_sets.keys():
            curr_longest = 1
            curr_val = num
            while curr_val+1 in nums_set: 
                curr_longest += 1
                curr_val += 1
            if out < curr_longest:
                out = curr_longest

        return out