class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        num_partition = len(s) + 1
        can_break = [False] * num_partition
        can_break[0] = True
        words = set(wordDict)
        max_word_length = max(len(word) for word in words)


        for end_index in range(1, len(s) + 1):
            for start_index in range(max(0, end_index - max_word_length), end_index):
                substring = s[start_index:end_index]
                if can_break[start_index] and substring in words:
                    can_break[end_index] = True
        

        return can_break[-1]
