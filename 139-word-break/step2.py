class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        num_partition = len(s) + 1 # sの各文字間の仕切りの数
        can_break = [False] * num_partition # 仕切りの最後で分割可能(True)なら最終的に分割可能
        can_break[0] = True # len(s)が0なら必ず分割可能
        
        for end_i in range(1, len(s) + 1):
            for start_i in range(end_i):
                substring = s[start_i:end_i]
                # 新たな部分文字列が見つかり、その直前の仕切りで分割可能
                if can_break[start_i] and substring in wordDict:
                    can_break[end_i] = True
                    break

        return can_break[len(s)]
