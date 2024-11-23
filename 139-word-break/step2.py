class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        partition_nums = len(s) + 1 # sの各文字間の仕切りの数
        can_break = [False] * partition_nums # 動的計画法のメモのため
        can_break[0] = True # len(s)が0なら必ず分割可能
        
        for end_i in range(1, len(s)+1):
            for start_i in range(end_i):
                substring = s[start_i:end_i]
                # 新たな部分文字列が見つかり、その直前の仕切りで分割可能
                if can_break[start_i] and substring in wordDict:
                    can_break[end_i] = True
                    break

        return can_break[len(s)]
