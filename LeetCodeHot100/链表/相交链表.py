# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set1=set()
        cur=headA
        while(cur):
            set1.add(cur)
            cur=cur.next
        cur=headB
        while(cur):
            if(cur in set1):
                return cur
            cur=cur.next
        return None






if __name__ == '__main__':
    solution=Solution()

