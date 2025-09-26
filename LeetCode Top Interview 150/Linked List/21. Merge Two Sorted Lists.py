# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #T=O(l1+l2)), S=O(l1+l2)
        dummy_head=ListNode()
        curr=dummy_head
        while list1 and list2:
            num1=list1.val
            num2=list2.val
            newNode = ListNode()
            if num1<=num2:
                newNode.val=num1
                list1=list1.next
            else:
                newNode.val=num2
                list2=list2.next
            curr.next=newNode
            curr=newNode
        if not list1:
            curr.next=list2
        else:
            curr.next=list1
        return dummy_head.next


if __name__ == '__main__':
    solution=Solution()
    node1_1=ListNode(1)
    node1_2=ListNode(2)
    node1_3=ListNode(4)
    # node1_4=ListNode(9)
    # node1_5=ListNode(9)
    # node1_6=ListNode(9)
    # node1_7=ListNode(9)
    node1_1.next=node1_2
    node1_2.next=node1_3

    node2_1=ListNode(1)
    node2_2=ListNode(3)
    node2_3=ListNode(4)
    # node2_4=ListNode(9)
    node2_1.next=node2_2
    node2_2.next=node2_3
    print(solution.mergeTwoLists(node1_1,node2_1))
