class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Fix 1: Sort the input array so anagrams are adjacent to each other
        strs = sorted(strs, key=sorted)
        
        res = []
        sub_group = []
        
        for word in strs:
            if not sub_group:
                sub_group.append(word)
            # Fix 2: Check if the current word is an anagram of the group's first word
            elif sorted(word) == sorted(sub_group[0]):
                sub_group.append(word)
            else:
                # Fix 3: Use append() instead of index assignment res[i]
                res.append(sub_group)
                sub_group = [word] # Start the next group with the current word
                
        # Fix 4: Append the very last group after the loop finishes
        if sub_group:
            res.append(sub_group)
            
        return res



                



            


