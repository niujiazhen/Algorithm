# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=ListNode()#use dummy head to avoid checking edge cases
        dummy_head.next=head
        cur=dummy_head
        while cur.next:
            isDelete=0#represent whethere to delete the node
            while cur.next.next and cur.next.val==cur.next.next.val:#this loop could remove duplicated element
                cur.next=cur.next.next
                isDelete=1
            if isDelete:#if we find duplicated elements, we have to remove the first one
                cur.next=cur.next.next
            else:
                cur=cur.next#otherwise just move forward
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