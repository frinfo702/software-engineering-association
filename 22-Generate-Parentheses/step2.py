class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        def backtrack(current_parenthesis, open_count, close_count):
            if len(current_parenthesis) == 2 * n:
                result.append("".join(current_parenthesis))
                return

            # ( can be added
            if open_count < n:
                current_parenthesis.append("(")
                backtrack(current_parenthesis, open_count + 1, close_count)
                current_parenthesis.pop()

            # ) can be added
            if open_count > close_count:
                current_parenthesis.append(")")
                backtrack(current_parenthesis, open_count, close_count + 1)
                current_parenthesis.pop()

        backtrack([], 0, 0)
        return result
