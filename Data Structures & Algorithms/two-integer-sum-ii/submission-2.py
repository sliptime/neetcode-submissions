class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_set = defaultdict(int)

        for i, num in enumerate(numbers):
            compliment = target - num
            if compliment != num:
                if compliment in number_set:
                    if num < compliment:
                        return [i+1, number_set.get(compliment)+1]
                    else:
                        return [number_set.get(compliment)+1, i+1]
            number_set[num] = i

        return