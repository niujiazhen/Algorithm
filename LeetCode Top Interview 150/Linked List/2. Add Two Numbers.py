# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #T=O(max(m,n)), S=O(max(m,n))
        # cur_l1,cur_l2=l1,l2 #listnode
        # str_l1=str_l2=""
        # while cur_l1:#get the num of l1
        #     str_l1+=str(cur_l1.val)
        #     cur_l1=cur_l1.next
        # while cur_l2:#get the num of l2
        #     str_l2+=str(cur_l2.val)
        #     cur_l2=cur_l2.next
        # str_l1=str_l1[::-1]#reverse the str to get the real add num
        # str_l2=str_l2[::-1]
        # ans=str(int(str_l1)+int(str_l2))#the ans after adding
        # ans=ans[::-1]#reverse the ans
        #
        # head_node=ListNode()
        # prev_node=head_node
        # for i in range(len(ans)):
        #     cur_node=ListNode(int(ans[i]))
        #     prev_node.next=cur_node
        #     prev_node=cur_node
        # return head_node.next

        # T=O(max(m,n)), S=O(max(m,n))
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0 #to add to the next iteration
        l1_val=0
        l2_val=0
        while l1 or l2 or carry!=0:#carry != 0 is due to the last add operation may create a carry
            if l1:
                l1_val=l1.val
            else:
                l1_val=0
            if l2:
                l2_val=l1.val
            else:
                l2_val=0
            sum=l1_val+l2_val+carry
            carry=sum//10 #for the next iteration
            newNode = ListNode(sum % 10)
            curr.next = newNode
            curr = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next






if __name__ == '__main__':
    solution=Solution()
    node1_1=ListNode(2)
    node1_2=ListNode(4)
    node1_3=ListNode(3)
    # node1_4=ListNode(9)
    # node1_5=ListNode(9)
    # node1_6=ListNode(9)
    # node1_7=ListNode(9)
    node1_1.next=node1_2
    node1_2.next=node1_3

    node2_1=ListNode(5)
    node2_2=ListNode(6)
    node2_3=ListNode(4)
    # node2_4=ListNode(9)
    node2_1.next=node2_2
    node2_2.next=node2_3
    print(solution.addTwoNumbers(node1_1,node2_1))