# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=ListNode()
        cur=dummy_head
        while(list1 and list2):
            node=ListNode()
            if(list1.val<list2.val):
                node.val=list1.val
                list1=list1.next
            else:
                node.val=list2.val
                list2=list2.next
            cur.next=node
            cur=cur.next

        if(list1):
            cur.next=list1
        else:
            cur.next=list2
        return dummy_head.next







if __name__ == '__main__':
    linklist1_node1=ListNode(1)
    linklist1_node2=ListNode(2)
    linklist1_node3=ListNode(4)
    linklist1_node1.next=linklist1_node2
    linklist1_node2.next=linklist1_node3

    linklist2_node1=ListNode(1)
    linklist2_node2=ListNode(3)
    linklist2_node3=ListNode(4)
    linklist2_node1.next=linklist2_node2
    linklist2_node2.next=linklist2_node3

    solution=Solution()
    solution.mergeTwoLists(linklist1_node1,linklist2_node1)