# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Merge Sort: T=O(nlogn) S=O(logn)
        if not head or not head.next:
            #if the list only contain 1/0 node, return the original list
            return head
        #Divide
        midNode=self.getMid(head)
        #Conquer
        leftList=self.sortList(head)
        rightList=self.sortList(midNode)
        #Combine
        return self.merge(leftList,rightList)

    def getMid(self,head:ListNode)->ListNode:
        #use fast and slow pointers to truncate the LinkedList and get the middleLeft node
        fast=slow=head
        midPrev=None#the node before mid node
        while fast and fast.next:
            midPrev=slow
            slow=slow.next
            fast=fast.next.next
        midPrev.next=None#truncate the LinkedList to two list
        return slow
    def merge(self,list1:ListNode,list2:ListNode)->ListNode:
        #merge two sorted list into one list
        dummy_head=ListNode(-1)
        cur=dummy_head
        while list1 and list2:
            if list1.val<list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        if list1:
            cur.next=list1
        else:
            cur.next=list2
        return dummy_head.next










if __name__ == '__main__':
    solution=Solution()
    node1=ListNode(4)
    node2=ListNode(2)
    node3=ListNode(1)
    node4=ListNode(3)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    print(solution.sortList(node1))
