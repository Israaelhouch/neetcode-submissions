class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        if len(s)== len(t):
            for letter in s:
                if letter not in seen:
                    seen.add(letter)
                    if s.count(letter)!= t.count(letter):
                        return False
            return True
                
        else:
            return False

        