# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int)->ListNode:
    # 快慢指针
    dummyHead=ListNode(-1)
    dummyHead.next=head
    fast=slow=dummyHead


    for i in range(n):
        fast=fast.next

    while fast.next:
        fast=fast.next
        slow=slow.next

    # 现在slow节点是需要删除的
    slow.next=slow.next.next

    return dummyHead.next






if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(removeNthFromEnd(node1, 2))