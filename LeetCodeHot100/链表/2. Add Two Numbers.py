# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

def addTwoNumbers(l1: ListNode, l2: ListNode)->ListNode:
    # Edge Case
    if not l1:
        return l2
    if not l2:
        return l1

    # Two Pointers
    dummyHead=ListNode(-1,None)
    cur=dummyHead
    carry=0# 进位

    print(10%10)
    while l1 or l2 or carry!=0:
        val_1,val_2=0,0
        if l1:# 两边都有加数
            val_1=l1.val
            l1=l1.next
        if l2:
            val_2=l2.val
            l2=l2.next
        num = val_1 + val_2 + carry# 计算当前为止的加数
        cur.next = ListNode(num%10, None)
        carry = num // 10# 计算进位
        cur = cur.next

    return dummyHead.next








if __name__ == '__main__':
    node1 = ListNode(9)
    node2 = ListNode(9)
    node3 = ListNode(9)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    print(addTwoNumbers(node1,node4))