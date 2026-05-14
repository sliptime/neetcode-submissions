class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_set = defaultdict(int)

        i = 0
        number_set[numbers[i]] = i
        i += 1
        while i < len(numbers):
            compliment = target - numbers[i]
            if compliment != numbers[i]:
                if compliment in number_set:
                    if numbers[i] < compliment:
                        return [i+1, number_set.get(compliment)+1]
                    else:
                        return [number_set.get(compliment)+1, i+1]
            number_set[numbers[i]] = i
            i += 1

        return