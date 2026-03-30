# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def reverseList(head: ListNode)->ListNode:
    # Edge Case
    if not head:
        return None

    # prev+cur节点:
    # T=O(n) S=O(1)
    prev=None# 记录cur前一个节点
    cur=head
    while cur:# 开始反转
        temp=cur.next
        cur.next=prev# cur指向前一个节点，进行反转
        prev=cur# prev记录当前cur
        cur=temp# cur指向下一个节点

    # 最后cur为空，链表头应该是cur的前一个节点prev
    return prev

node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
print(reverseList(node1).val)









