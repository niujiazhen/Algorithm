# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def getIntersectionNode(headA:ListNode, headB:ListNode)->ListNode:
    # HashTable T=O(n) S=O(n)
    # hash=set()
    # curA=headA
    # curB=headB
    #
    # while curA:
    #     hash.add(curA)
    #     curA=curA.next
    #
    # while curB:
    #     if curB in hash:
    #         return curB
    #     curB=curB.next
    #
    # return None

    # Two Pointer T=O(n) S=O(1)
    # Edge Case
    if not headA or not headB:
        return None

    # Basic Solution
    curA=headA
    curB=headB
    lenA=0
    lenB=0

    # 计算两个链表长度
    while curA:
        lenA+=1
        curA=curA.next

    while curB:
        lenB+=1
        curB=curB.next

    # 让长的链表先走差值步
    curA=headA
    curB=headB

    if lenA>lenB:
        for i in range(lenA-lenB):
            curA=curA.next
    else:
        for i in range(lenB-lenA):
            curB=curB.next

    # 现在两个链表距离结尾距离相同，同时遍历找相交点

    while curA and curB:
        if curA==curB:
            return curA
        curA=curA.next
        curB=curB.next

    return None





node1_1=ListNode(4)
node1_2=ListNode(1)
node1_1.next=node1_2

node2_1=ListNode(5)
node2_2=ListNode(6)
node2_3=ListNode(1)
node2_1.next=node2_2
node2_2.next=node2_3

node1=ListNode(8)
node2=ListNode(4)
node3=ListNode(5)

node1_2.next=node1
node2_3.next=node1

print(getIntersectionNode(node1_1,node2_1).val)