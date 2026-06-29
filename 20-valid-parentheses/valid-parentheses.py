class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char not in bracket_map:
                stack.append(char)
            if char in bracket_map:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top !=  bracket_map[char]:
                    return False
        return len(stack) == 0

        