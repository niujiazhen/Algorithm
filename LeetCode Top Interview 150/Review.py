# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Merge Sort: T=O(nlogn) S=O(logn)
        #We use Divide and Conquer
        def getMid(node:ListNode)->ListNode:
            #We use fast and slow pointer to get the midNode and truncate the LinkedList into two equal parts
            fast=slow=head
            midPrev=None#the node before midNode
            while fast and fast.next:
                midPrev=slow
                slow=slow.next
                fast=fast.next.next
            midPrev.next=None#truncate the LinkedList
            return slow

        def merge(node1:ListNode,node2:ListNode)->ListNode:
            dummy_head=ListNode(-1)
            cur=dummy_head
            while node1 and node2:
                if node1.val<node2.val:
                    cur.next=node1
                    node1=node1.next
                else:
                    cur.next=node2
                    node2=node2.next
                cur=cur.next
            if node1:
                cur.next=node1
            else:
                cur.next=node2
            return dummy_head.next

        #Edge Case:if the LinkedList size is 1 or 0, just return the original node
        if not head or head.next is None:
            return head

        #Divide
        mid=getMid(head)
        #Conquer
        leftLinkedList=self.sortList(head)
        rightLinkedList=self.sortList(mid)
        #Combine
        return merge(leftLinkedList,rightLinkedList)









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
