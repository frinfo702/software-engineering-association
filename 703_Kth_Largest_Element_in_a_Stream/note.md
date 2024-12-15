# step1
- まず思いつくのは、与えられた配列をいちいちソートして、前からk番目の要素を返すやり方
```python
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums.copy()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
> [!NOTE]
> pythonはリストなどミュータブルなオブジェクトは参照渡しされるので`self.nums = nums`みたいな
> 書き方だと引数を書き換えるので受けてからすると意図しない動作に感じさせる
- これでも一応通る
- time complexity: O(nlogn) (n: numsの要素数)
- space complexity: O(n) (n: numsの要素数)
- 改善案
  - code complexity
  - memory
  - speed
- このcode complexityの改善は見込めないので、memory, speedの観点から考える
- 特に、問題のタイプ上add()の方は何度も呼び出しがかかっていそうなのでこっちを改善したい
- 時間計算量は分からないが、空間計算量に関しては後ろからkこの要素しかいらないので削減のアイデアが思い浮かぶのでこれを考える
- __init__()の中で降順でk番目までの要素だけを切り出しておいて、add()の中で挿入位置を調べて挿入みたいなのも考えたがここのオーバーヘッドを少しでも無くしたいので、だったら初めから__init__ないで適切なデータ構造を使う方がいいのでは->heapの使い方を調べた
```python
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            # サイズをkに調整
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]  # ヒープの根の要素がk番目に大きい値


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

```
- time complexity
  - init: O(n logk) (n: 初期配列の長さ, k: ヒープのサイズ)
  - add: O(logk) (k: ヒープのサイズ)
- space complexity: O(k) 
- n > kなのでmemoryの観点からはこっちのが良さそう。code complexityもたいして変わっていない。speedも早くなった

# step2
- 変数名をk -> sizeに変更
    - -> `        if len(self.heap) < self.size:` イメージとしてはlen(heap)がsizeと等しいはずなのに、これでは変な感じがするので、Kthに変更

- whileで回す部分は、渡される値の範囲が決まっているので、狭めるのが良さそう。ただ、この場合step1のwhileの書き方に何か不都合はあるのでしょうか
- heappushpopがあるらしい。こっちの方が効率がいいと書いてある。
- https://docs.python.org/3/library/heapq.html#heapq.heappushpop
- この場合ならどちらにしろwhileでの書き方は変えざるを得ない
```python
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.size = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            # サイズをkに調整
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

```
- これまではそもそも新たな最小値になり得ない数もpush & popしていたがそもそもpushをしないようにした
  
- quickselectというのを使った解法もあるらしい
- (後でみます...)

# step3
- 繰り返し提出
- step2のコードで提出した
- 何回かheappushなどを単にpushと書いてしまった
