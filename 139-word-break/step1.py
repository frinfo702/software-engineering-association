class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1) # 動的計画法のメモのため
        dp[0] = True # len(s)が0なら必ず分割可能
        words = set(wordDict)
        max_word_length = max(len(word) for word in words)

        for end_index in range(1, len(s) + 1):
            for start_index in range(max(0, end_index - max_word_length) , end_index):
                if dp[start_index] and s[start_index:end_index] in wordDict:
                    dp[end_index] = True
                    break

        return dp[-1]

