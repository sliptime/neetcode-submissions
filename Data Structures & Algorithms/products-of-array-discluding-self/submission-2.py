class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        pre_mult = 1
        for i in range(len(nums)):
            output[i] = pre_mult
            pre_mult *= nums[i]

        post_mult = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post_mult
            post_mult *= nums[i]
        return output
