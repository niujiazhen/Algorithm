# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List
from typing import Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # T=O(Nk) N is the number of nodes of all LinkedList, k is the number of LinkedList
        # S=O(1)
        # Edge Case
        if not lists:
            return None
        curList=lists[0]
        for i in range(1,len(lists)):
            curList=self.merge(curList,lists[i])
        return curList
    def merge(self,node1:ListNode,node2:ListNode)->ListNode:
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

if __name__ == '__main__':
    solution=Solution()

    node1_1=ListNode(1)
    node1_2=ListNode(4)
    node1_3=ListNode(5)
    node1_1.next=node1_2
    node1_2.next=node1_3

    node2_1=ListNode(1)
    node2_2=ListNode(3)
    node2_3=ListNode(4)
    node2_1.next=node2_2
    node2_2.next=node2_3

    node3_1=ListNode(2)
    node3_2=ListNode(6)
    node3_1.next=node3_2

    print(solution.mergeKLists([]))