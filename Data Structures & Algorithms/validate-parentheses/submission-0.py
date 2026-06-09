class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map: # if open parenthesis
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: # stack of -1 is last value just added
                return False
            stack.pop()

        return not stack

        

            