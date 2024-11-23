# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # サイクルがあるかを判定
        fast = head
        slow = head

        has_cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break
        
        # サイクルを持たない場合
        if has_cycle != True:
            return None

        # 両方の速度を1 [node/回]に変更、一方はheadへ戻す
        intersect = fast
        restart = head
        while intersect != restart:
            intersect = intersect.next
            restart = restart.next
        
        return intersect
