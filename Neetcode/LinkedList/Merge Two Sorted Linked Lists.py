from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # T=O(m+n) S=O(1)
        dummy_head=ListNode()
        cur=dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next=list1
        else:
            cur.next=list2

        return dummy_head.next



if __name__ == '__main__':
    solution=Solution()
    node1_1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(3)
    node2_1 = ListNode(4)
    node2_2 = ListNode(5)
    node2_3 = ListNode(5)

    node1_1.next=node1_2
    node1_2.next=node1_3
    node2_1.next=node2_2
    node2_2.next=node2_3
    print(solution.mergeTwoLists(node1_1,node2_1))