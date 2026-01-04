# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=ListNode(-1,head)
        prev=dummy_head
        cur=dummy_head.next

        while cur:
            if cur.next and cur.val==cur.next.val:#If we find duplicated nums
                num=cur.val# records the duplicated value
                while cur and cur.val==num:
                    cur=cur.next
                prev.next=cur
            else:
                prev=cur
                cur=cur.next
        return dummy_head.next



if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    print(solution.deleteDuplicates(node1))