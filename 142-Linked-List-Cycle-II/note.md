# step1
- 以前にlinked listのサイクルを見つける問題を解いたことがあるのでそれを活かせないか
- その時は二つのポインタで追いかけっこをして、一方が他方に追いつくことができたらサイクルがあると判定していた
- このときのものを流用してサイクルが見つかった時点でのnode objectを返すようにすればいいのではないか

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            if fast == slow:
                return fast
            fast = fast.next.next
            slow = slow.next
        
        return None
```
で提出
```
head = [3,2,0,-4], pos = 1
```
の場合が通らなかった

- 多分、サイクルの長さの偶奇によってうまくいくときといかない時が出ている
- `slow`がサイクルの先頭(表現怪しい)にあればそこで`fast`が追いつけば判定はうまくいくが、`fast`はあくまで1こ飛ばしで移動するため、サイクルの検出がいつかはうまくいっても、それが綺麗に`slow`がサイクルの開始点で重なるかはlinked listの形による
- サイクルの長さの偶奇により処理の順番を分岐して判定できるようにしようかと考えたが、サイクルがどこから始まり長さはいくらかがわからないので却下
- サイクルの長さではなくて、`len(linked list)`, `pos`の2要素で決まる
- 5分経過したので解答を見て、理解できたら書くを繰り返す
- 一度であったら、そこから速度を同じにして一方をheadに戻し、再度出会ったところを返すと答えになるらしい。

> [!NOTE]
> [参考にした動画](https://www.youtube.com/watch?v=pfA0VuvwpVg)

- headに戻す理由がわからず、計算してみると以下の理屈で理解はできたがどうやってこれを直感的に気づくのかは理解できないまま

> [!NOTE]
> L：リストの先頭からサイクル開始点までの距離（ノード数）
> C：サイクルの周長（サイクルを一周するのに必要なノード数）
> X：サイクル開始点から slow と fast が最初に出会った地点までの距離
> ポインタの移動距離：
> slow が移動した総距離：L + X
> fast が移動した総距離：L + X + nC （n はサイクルを周回した回数）
> しかし、fast は slow の2倍の速度で移動しているため：
> 
> fastの移動距離 = 2 * slowの移動距離なので L + X +nC = 2(L+X)
> これを整理すると：L = nC + X 
> つまり、L はサイクルの周長 C の整数倍に X を加えたもの
> 
> サイクル開始点を見つける手順：
> slow をリストの先頭 head に戻し、fast は出会った地点にそのまま待機
> 両方のポインタを一度に1つのノードずつ進める
> slow がサイクル開始点に到達するまでの距離は L 
> 先ほどの式より、L = nC + X であり、fast は既に L + X 進んでいる
> fast は追加で L 進むと、L + X + L = 2L + X となり、これはサイクルをさらに nC 周回した位置となる
> したがって、両方のポインタはサイクル開始点で再び出会う

# step2
- 二者択一の部分を条件分岐でまとめた

# step3