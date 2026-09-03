class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack =[]
        for i in s:
            if i in close_to_open:

                if not stack:
                    return False

                if stack[-1] != close_to_open[i]:
                    return False
                stack.pop()
            
            else:
                stack.append(i)
        
        if stack:
            return False
        
        return True