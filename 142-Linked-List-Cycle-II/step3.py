# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # サイクルを持つか判定
        has_cycle = False

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break

        # サイクルの有無で分岐

        if not has_cycle:
            return None

        intersect = fast
        restart = head

        while intersect != restart:
            intersect = intersect.next
            restart = restart.next

        return intersect
