class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_set = {}

        i = 0
        number_set[numbers[i]] = i
        i = 1
        while i < len(numbers):
            if target - numbers[i] != numbers[i]:
                if target - numbers[i] in number_set:
                    if numbers[i] < target - numbers[i]:
                        return [i+1, number_set.get(target - numbers[i])+1]
                    else:
                        return [number_set.get(target - numbers[i])+1, i+1]
            number_set[numbers[i]] = i
            i += 1

        return