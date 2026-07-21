# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #T=O(n), S=O(n)
        # hash=set()
        # while head:
        #     if head in hash:
        #         return True
        #     hash.add(head)
        #     head=head.next
        # return False

        #Fast and Slow Pointers T=O(n), S=O(1)
        fast=slow=head
        while fast and fast.next:# if fast or fast.next ==null, it means the linked list has an end
            slow=slow.next
            fast=fast.next.next
            if fast==slow:#means the linked list is a cycle so the fast and slow pointers could meet each other (the fast pointer laps the slow pointer)
                return True
        return False



if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(solution.hasCycle(node1))