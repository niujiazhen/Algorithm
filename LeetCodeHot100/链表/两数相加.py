# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1List=[]
        num2List=[]
        while(l1):
            num1List.append(str(l1.val))
            l1=l1.next
        while (l2):
            num2List.append(str(l2.val))
            l2 = l2.next

        num1List.reverse()
        num2List.reverse()
        num1=int("".join(num1List))
        num2=int("".join(num2List))
        num3=num1+num2
        resultLinkList=ListNode()
        cur=resultLinkList
        while(num3>0):
            cur.val=num3%10
            num3//=10
            if(num3==0):
                break
            cur.next=ListNode()
            cur=cur.next
        return resultLinkList








if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    solution=Solution()
    print(solution.addTwoNumbers(node1,node4))