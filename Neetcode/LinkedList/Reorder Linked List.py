from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:




if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(6)
    node4 = ListNode(8)
    node5 = ListNode(10)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(solution.reorderList(node1))