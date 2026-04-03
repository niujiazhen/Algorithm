# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode)->ListNode:
    # Edge Case
    if not head:
        return None

    # 虚拟头节点
    dummyHead=ListNode(-1)
    dummyHead.next=head
    cur=dummyHead

    while cur.next and cur.next.next:
        temp=cur.next.next.next # 记录要链接的节点
        leftNode=cur.next
        rightNode=cur.next.next
        cur.next=rightNode
        rightNode.next=leftNode
        leftNode.next=temp
        cur=cur.next.next

    return dummyHead.next




if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(swapPairs(node1))
