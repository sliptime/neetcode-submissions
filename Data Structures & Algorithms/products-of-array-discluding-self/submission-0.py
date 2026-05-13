class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult_val = 1
        a_zero = False
        are_zeros = False
        out = []
        for num in nums:
            if num == 0:
                if a_zero:
                    are_zeros = True
                a_zero = True
            else:
                mult_val *= num
        for num in nums:
            if num == 0 and not are_zeros:
                out.append(int(mult_val))
            elif a_zero:
                out.append(int(0))
            else:
                out.append(int(mult_val/num))
        return out
