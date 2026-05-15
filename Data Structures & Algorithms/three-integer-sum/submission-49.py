class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtn = []

        for i, mid in enumerate(nums[1:len(nums)-1], 1):
            j = i-1
            k = i+1
            while j >= 0 and k <= len(nums)-1:
                if nums[j] + nums[k] == -mid:
                    if rtn and nums[i] == nums[i-1] and nums[j] != nums[i]:
                        break
                    if not rtn or [nums[j], nums[i], nums[k]] != rtn[-1] :
                        rtn.append([nums[j], nums[i], nums[k]])
                    if j > 0:
                        j -= 1
                    else:
                        k += 1
                elif nums[j] + nums[k] > -mid:
                    j -= 1
                elif nums[j] + nums[k] < -mid:
                    k += 1
        return rtn


        