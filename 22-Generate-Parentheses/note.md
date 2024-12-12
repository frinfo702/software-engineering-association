# step1
- まず思いつくのは順列を作ってそれぞれのパターンに対して有効な括弧かを確かめる
  - 計算量大きいので他のを考える
- まず開き括弧を一つ目に据えるのは確定、これを繰り返してその状態における有効な配置のみを繰り返していく
- 推移を樹形図で表現できるので、木構造が有効な気がする
- 調べると実装上再帰やスタックを使うらしい。また、逐一その時点での解が有効か無効か判断しながら計算を進めるのをバックトラッキングというらしい
- (がまだ追加できる時、追加した場合(の数が)の数以上であればそれぞれ`(`, `)`を追加

はじめ、
```python
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

            # (が追加可能
            if open_count < n:
                current_parenthesis += '('
                open_count += 1
                backtrack(current_parenthesis, open_count, close_count)

            if open_count > close_count:
                current_parenthesis += ')'
                close_count += 1
                backtrack(current_parenthesis + ")", open_count, close_count + 1)

        open_count = 0  # 使用した(の数
        close_count = 0  # 使用した)の数
        current_parenthesis = ""
        result = []
        backtrack(current_parenthesis, open_count, close_count)
        return result
```

と書いたがこれだとスタックされていく関数の戻り先の情報に括弧の追加や使用した括弧の個数の情報が乗らずに、各再帰が独立した探索ではなくなり重複が発生してしまった

## step2

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # ( can be added
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1,close_count)
                current.pop()

            # ) can be added
            if open_count > close_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result
```
- current部分をstrではなくてlistでやるやり方も考えた。
- やや冗長になるがバックトラッキングがより明示的に思えたのでこっちにした
- どっちがいいかの基準がわからなかった
	- Leetcode上でかかる時間はどちらも同じぐらい

# step3
- 繰り返し提出
- 何をやりたいかが書いているうちにブレないようにメモ的な感じでいちいち変数名を置くことにした
```python
        current_parenthesis = []
        open_count = close_count = 0
```
