class Solution:
    def isValid(self, s: str) -> bool:
        brackets_pair = {"(": ")", "{": "}", "[": "]"}
        brackets_stack = []

        for char in s:
            if char in brackets_pair:
                brackets_stack.append(char)
                continue
            if not brackets_stack:
                return False
            if brackets_pair[brackets_stack[-1]] != char:
                return False
            brackets_stack.pop()

        return not brackets_stack
