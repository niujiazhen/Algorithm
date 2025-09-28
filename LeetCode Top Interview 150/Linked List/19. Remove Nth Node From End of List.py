# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head=ListNode()#use the dummy head to save the previous node before the node to be deleted
        dummy_head.next=head
        fast=slow=dummy_head
        #the following two steps is to find the node to be deleted
        while n>0:
            fast=fast.next
            n-=1
        while fast.next:
            fast=fast.next
            slow=slow.next

        slow.next = slow.next.next#delete the node
        return dummy_head.next


if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(solution.removeNthFromEnd(node1, 2))