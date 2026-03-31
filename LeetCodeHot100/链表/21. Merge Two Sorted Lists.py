# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode)->ListNode:
    # Edge Case
    if not list1:
        return list2
    if not list2:
        return list1

    # Two Pointers
    # T=O(n) S=O(1)
    dummyHead=ListNode(-1,None)
    cur=dummyHead

    while list1 and list2:
        if list1.val<list2.val:
            cur.next=list1
            list1=list1.next
        else:
            cur.next=list2
            list2=list2.next
        cur=cur.next

    if list1:
        cur.next=list1
    else:
        cur.next=list2

    return dummyHead.next







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

    mergeTwoLists(linklist1_node1,linklist2_node1)