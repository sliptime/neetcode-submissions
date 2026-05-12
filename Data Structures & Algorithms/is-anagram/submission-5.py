class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countAnagram = [0] * 128;
        for i in range(len(s)):
            countAnagram[ord(s[i])] += 1
            countAnagram[ord(t[i])] -= 1
        for counts in countAnagram:
            if counts != 0:
                return False

        return True
                