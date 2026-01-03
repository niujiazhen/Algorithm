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
        # Reverse the LinkedList in place
        # Edge Case
        if not head:
            return None
        prev=None# records the node before cur
        cur=head

        # We first find the first element of the reversed zone
        while left>1:
            prev=cur
            cur=cur.next
            left-=1
            right-=1

        conn=prev # records the last prev node before reversing
        tail=cur # after reversing the list, the tail node is the head node cur

        # Then we reverse the LinkedList for right times in reversed zone
        while right>0:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            right-=1

        # Connect the head of reversed zone list
        if conn:# conn might be None
            conn.next=prev
        else:
            head=prev

        # Connect the tail of reverse zone list
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

