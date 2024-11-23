class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        partition_length = len(s) + 1
        can_break = [False] * partition_length
        can_break[0] = True

        for end_i in range(1, len(s)+1):
            for start_i in range(end_i):
                substring = s[start_i:end_i]
                if can_break[start_i] and substring in wordDict:
                    can_break[end_i] = True
        
        return can_break[-1]
