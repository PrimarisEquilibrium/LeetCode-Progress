class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}

        for letter in s:
            if letter not in first:
                first[letter] = 1
            else:
                first[letter] += 1
        
        for letter in t:
            if letter not in second:
                second[letter] = 1
            else:
                second[letter] += 1
        
        if first == second: return True
        return False