class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        num_partition = len(s) + 1
        can_break = [False] * num_partition
        can_break[0] = True
        wordSet = set(wordDict)

        for end_i in range(1, len(s) + 1):
            for start_i in range(end_i):
                substring = s[start_i:end_i]
                if can_break[start_i] and substring in wordSet:
                    can_break[end_i] = True
        
        return can_break[-1]
