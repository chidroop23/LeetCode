class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in Map:
                if stack and stack[-1] == Map[c]:  # Macthing the closed parenthises and open parenthises
                    stack.pop() # then we pop  from the stack if they match 
                else:
                    return False # If they dont match or if the stack is empty then return false
            else:
                stack.append(c) #if we find an open parenthises then we keep appending to the stack and keep going
        return True if not stack else False # Once we gone through every character, we can only return true if our stack is empty 
            