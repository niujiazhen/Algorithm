# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        cur=head
        temp=ListNode()
        while(cur):
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre


if __name__ == '__main__':
    solution=Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    solution.reverseList(node1)

