# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result=[]
        dummy_head=ListNode()
        dummy_head.next=head
        cur=dummy_head
        while(cur.next):
            result.append(cur.next.val)
            cur=cur.next
        n=len(result)
        # for i in range(n//2):
        #     if(result[i]!=result[n-i-1]):
        #         return False
        # return True
        result_reverse=list(reversed(result))
        return result==result_reverse








if __name__ == '__main__':
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(2)
    node4=ListNode(1)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    solution=Solution()
    print(solution.isPalindrome(node1))
