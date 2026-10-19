class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        occurences = {}
        for char in s:
            if char in occurences:
                occurences[char] += 1
            else:
                occurences[char] = 1
        for char in t:
            if char not in occurences:
                return False
            occurences[char] -= 1
            if occurences[char] < 0:
                return False
        return True

