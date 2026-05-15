class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtn = []

        for i, start in enumerate(nums):
            if i > 0 and start == nums[i - 1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] > -start:
                    k -= 1
                elif nums[j] + nums[k] < -start:
                    j += 1
                else:
                    rtn.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
        return rtn


        