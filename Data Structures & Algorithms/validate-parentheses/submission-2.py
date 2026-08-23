class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{',']':'['}
        stack = []
        i = 0
        for i in s:
            if i == ')' or i == '}' or i == ']':
                if not stack:
                    return False
                if stack.pop() != brackets[i]:
                    return False
            else:
                stack.append(i)
        return True if not stack else False