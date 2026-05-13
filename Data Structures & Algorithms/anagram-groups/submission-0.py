class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = [[0 for _ in range(128)] for _ in range(len(strs))]
        hashmap = {}
        output = []
        for i, string in enumerate(strs):
            for c in string:
                count[i][ord(c)] += 1
        output_id = 0
        for i, string in enumerate(strs):
            key = tuple(count[i])
            if key not in hashmap:
                hashmap[key] = output_id
                output.append([string])
                output_id += 1
            else:
                output[hashmap.get(key)].append(string)
        return output