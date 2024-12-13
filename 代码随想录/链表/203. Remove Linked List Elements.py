# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head=ListNode(0,next=head)
        cur=dummy_head
        while(cur.next):
            if(cur.next.val==val):
                cur.next=cur.next.next
            else:
                cur=cur.next
            if(cur==None):
                break

        return dummy_head.next




if __name__ == '__main__':
    solution=Solution()
    node1=ListNode(7)
    node2=ListNode(7)
    node3=ListNode(7)
    node4=ListNode(7)
    # node5=ListNode(4)
    # node6=ListNode(5)
    # node7=ListNode(6)

    node1.next=node2
    node2.next=node3
    node3.next=node4
    # node4.next=node5
    # node5.next=node6
    # node6.next=node7

    solution.removeElements(node1,7)