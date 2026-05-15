class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_char_index = [-1] * 128
        longest_non_repeating_string = 0
        start = 0
        for i in range(len(s)):
            char_code = ord(s[i])
            if last_char_index[char_code] >= start:
                start = last_char_index[char_code] + 1
            last_char_index[char_code] = i
            longest_non_repeating_string = max(longest_non_repeating_string, i - start + 1)

        return longest_non_repeating_string