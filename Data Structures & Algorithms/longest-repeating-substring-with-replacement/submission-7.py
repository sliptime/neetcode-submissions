class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq_char = 0
        longest_substr = 0

        for right, c in enumerate(s):
            count[c] += 1
            max_freq_char = max(max_freq_char, count[c])

            while (right - left + 1) - max_freq_char > k:
                count[s[left]] -= 1
                left += 1
            longest_substr = max(longest_substr, right-left+1)

        return longest_substr