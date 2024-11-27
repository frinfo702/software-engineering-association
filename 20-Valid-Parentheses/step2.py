class Solution:
    def isValid(self, s: str) -> bool:
        brackets_pair = {"(": ")", "{": "}", "[": "]"}
        brackets_stack = []

        for char in s:
            if char in brackets_pair:
                brackets_stack.append(char)
                continue
            # 閉じ括弧の時はスタックを見る
            elif char in brackets_pair.values():
                if not brackets_stack:
                    return False
                if brackets_pair[brackets_stack[-1]] != char:
                    return False
                brackets_stack.pop()

        return not brackets_stack
