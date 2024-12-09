# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        set1=set()
        cur=head
        while(cur):
            if(cur in set1):
                return cur
            set1.add(cur)
            cur=cur.next
        return None




if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    solution = Solution()
    print(solution.detectCycle(node1))
