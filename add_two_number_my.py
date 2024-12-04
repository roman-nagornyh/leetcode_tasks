class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        totalNode = ListNode()
        while l1 or l2:
            val1 = l1.val if l1.val else 0
            val2 = l2.val if l2.val else 0
            result = val1 + val2
            div_res =  result // 10




