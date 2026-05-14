class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_set = {}

        i = 0
        number_set[numbers[i]] = i
        i = 1
        while i < len(numbers):
            if target - numbers[i] != numbers[i]:
                if target - numbers[i] in number_set:
                    return [min(i+1, number_set.get(target - numbers[i])+1), max(i+1, number_set.get(target - numbers[i])+1)]
            number_set[numbers[i]] = i
            i += 1

        return