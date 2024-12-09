# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        pre=None
        while(cur):
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre









if __name__ == '__main__':
    solution=Solution()
