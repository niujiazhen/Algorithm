# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=lenB=0
        curA=headA
        curB=headB
        while(curA):
            lenA+=1
            curA=curA.next
        while(curB):
            lenB+=1
            curB=curB.next

        curA=headA
        curB=headB
        if(lenA>lenB):
            for i in range(lenA-lenB):
                curA=curA.next
            while(curA and curB):
                if(curA==curB):
                    return curA
                curA=curA.next
                curB=curB.next
            return None
        else:
            for i in range(lenB-lenA):
                curB=curB.next
            while (curA and curB):
                if (curA == curB):
                    return curA
                curA = curA.next
                curB = curB.next
            return None



if __name__ == '__main__':
    solution=Solution()
    node1=ListNode(4)
    node2=ListNode(1)
    node3=ListNode(5)
    node4=ListNode(6)
    node5=ListNode(1)
    node6=ListNode(8)
    node7=ListNode(4)
    node8=ListNode(5)

    node1.next=node2
    node2.next=node6
    node6.next=node7
    node7.next=node8
    node3.next=node4
    node4.next=node5
    node5.next=node6

    print(solution.getIntersectionNode(node1, node3))
