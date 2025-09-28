# Definition for singly-linked list.
import contextlib
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #T=O(n), S=O(1)
        if not head:
            return None

        #we first find the reverse zone
        prev=None
        cur=head
        while left>1:
            prev=cur
            cur=cur.next
            left-=1
            right-=1

        conn=prev#use to connect the head of the reversed linked list
        tail=cur#the tail of the reversed linked list

        while right>0:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            right-=1

        if conn:
            conn.next=prev
        else:
            head=prev

        tail.next=cur
        return head




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
    print(solution.reverseBetween(node1, 2, 4))

