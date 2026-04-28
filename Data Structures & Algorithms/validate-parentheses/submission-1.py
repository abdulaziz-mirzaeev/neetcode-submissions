class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                opening = stack.pop() if stack else None
                if opening != pairs[char]:
                    return False
        
        if stack:
            return False

        return True