# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # we set two dummy heads
        smallHead=ListNode()#node that smaller than x is connected to this node
        bigHead=ListNode()#node that bigger than x is connected to this node
        small=smallHead
        big=bigHead

        while head:
            if head.val<x:#if smaller, put it into the smallNode
                small.next=head
                small=small.next
            else:
                big.next=head
                big=big.next
            head=head.next

        big.next=None#after loop, the big node is the last node of the LinkedList
        #combine the two nodeLists
        small.next=bigHead.next

        return smallHead.next







if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(0)
    node5 = ListNode(2)
    node6 = ListNode(5)
    node7 = ListNode(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next=node6
    node6.next=node7
    print(solution.partition(node1,3))
