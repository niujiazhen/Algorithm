# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self,val:int):
        self.val=val
        self.next=None

def isPalindrome(head: ListNode)->bool:
    # Edge Case
    if not head:
        return False

    # Solution 1：Stack
    stack=[]
    cur=head
    while cur:
        stack.append(cur.val)
        cur=cur.next

    cur=head
    while cur:
        if cur.val != stack.pop():
            return False
        cur=cur.next
    return True







if __name__ == '__main__':
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(2)
    node4=ListNode(1)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    print(isPalindrome(node1))
