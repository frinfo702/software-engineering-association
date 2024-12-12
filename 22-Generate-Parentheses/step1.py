class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def backtrack(current_parenthesis, open_count, close_count):
            if len(current_parenthesis) == 2 * n:
                result.append(current_parenthesis)
                return

            # ( can be added
            if open_count < n:
                backtrack(current_parenthesis + "(", open_count + 1, close_count)

            if open_count > close_count:
                backtrack(current_parenthesis + ")", open_count, close_count + 1)

        open_count = 0  # Number of ( used
        close_count = 0  # Number of ) used
        current_parenthesis = ""
        result = []
        backtrack(current_parenthesis, open_count, close_count)
        return result
