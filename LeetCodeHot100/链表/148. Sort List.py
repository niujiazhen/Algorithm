from typing import List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


def sortList(head: ListNode)->ListNode:
    # Edge Case
    if not head:
        return None

    # T=O(nlogn) S=O(n)

    cur=head
    numList=[]
    while cur:
        numList.append(cur.val)
        cur=cur.next

    numList.sort()

    dummyHead=ListNode(-1)
    cur=ListNode(numList[0])
    dummyHead.next=cur
    for i in range(1,len(numList)):
        newNode=ListNode(numList[i])
        cur.next=newNode
        cur=newNode

    return dummyHead.next



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
sortList(node1)

