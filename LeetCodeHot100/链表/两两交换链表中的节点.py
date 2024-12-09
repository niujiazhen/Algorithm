# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=ListNode()
        dummy_head.next=head
        cur=dummy_head
        while(cur.next and cur.next.next):
            temp1 = cur.next
            temp2 = cur.next.next.next

            cur.next=cur.next.next
            cur.next.next=temp1
            cur.next.next.next=temp2

            cur=cur.next.next

        return dummy_head.next



if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solution=Solution()
    solution.swapPairs(node1)
