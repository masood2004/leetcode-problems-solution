class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if (len(s) % 2) == 0:
            for char in s:
                if char in '([{':
                    stack.append(char)
                else:
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == '(' and char == ')':
                        stack.pop()
                    elif stack[-1] == '{' and char == '}':
                        stack.pop()
                    elif stack[-1] == '[' and char == ']':
                        stack.pop()
                    else:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False
        else:
            return False
