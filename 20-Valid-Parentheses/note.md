# 思考メモ

## step1
- リストを分割して、片方は`(, {, [`を入れる。一方は`), }, ]`を入れていって、前者は後ろから。後者は前から見ていってそれぞれがペアの括弧になっているかを見ていく。
- 括弧管理としてスタックを使うのはいたって自然な発想だろうと思った

- また、ペアを辞書にして管理する方法も思いついたので、別途実装してみる

## step2
- ループ末尾の`continue`は不要だったので削除
- 括弧のリストだった部分を辞書に変更
- 最後の条件分岐でreturn していたところをreturn notにした

## step3
- leetcodeで書いているときに今回は括弧の記号以外はこないから`elif`じゃなくてもelseでかけるとして直した
