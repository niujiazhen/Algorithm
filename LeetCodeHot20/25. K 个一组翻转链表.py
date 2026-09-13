class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    # T=O(n) S=O(n/k)
    def reverseLinkedList(self, head: ListNode, k: int)->ListNode:
        # 翻转从head开始的前K个链表，返回翻转后的新链表头
        prev=None
        cur=head
        while k:
            t=cur.next
            cur.next=prev
            prev=cur
            cur=t
            k-=1

        return prev# 返回翻转后的链表头节点

    def reverseKGroup(self, head: ListNode, k: int)->ListNode:
        # 翻转每k个节点
        cnt=0
        cur=head
        # 先确定是否有k个节点
        while cur:
            cur=cur.next
            cnt+=1
            if cnt==k:
                break
        # 如果有k个节点，则先翻转前k个
        if cnt==k:
            reversedHead=self.reverseLinkedList(head,k)# 翻转前k个节点，然后用reversedHead记录翻转后的头节点
            head.next=self.reverseKGroup(cur,k)
            return reversedHead
        # 若没有k个节点，则直接返回当前部分的头节点
        return head