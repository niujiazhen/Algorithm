class DoublyListNode:#use a doubly list node to make add and remove operations in O(1)
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None#normal Linked List
        self.prev=None#to easily remove the current DoublyListNode by recording its previous node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dict={}#to store a hash map from key to DoublyListNode so that we can find the reference of a node in O(1) time
        self.head=DoublyListNode(-1,-1)#dummy_head
        self.tail=DoublyListNode(-1,-1)#dummy_tail
        self.head.next=self.tail
        self.tail.prev=self.head
        #the real Linked list is between head and tail

    def get(self, key: int) -> int:
        if key not in self.dict:#means the (key,value) node does not exist in dict
            return -1
        node=self.dict[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:#means the (key,value) node is already in the LinkedLis, so we remove the former one and put the updated at the tail
            old_node=self.dict[key]
            self.remove(old_node)
        node=DoublyListNode(key,value)
        self.add(node)#add the new node or updated node to the list
        self.dict[key]=node#add the (key,node) map to hashMap

        if len(self.dict)>self.capacity:#means we have to remove the least used node(the first node of the list)
            node_to_delete=self.head.next#remove the first node
            self.remove(node_to_delete)
            del self.dict[node_to_delete.key]


    def add(self,node:DoublyListNode):#add a new DoublyListNode to the tail of the LinkedList
        previous_end=self.tail.prev#the real tail element(or dummy_head if the list is empty)
        previous_end.next=node#add the new node at the end of the list
        node.prev=previous_end#set the prev of DoublyListNode
        node.next=self.tail#set the next of DoublyListNode
        self.tail.prev=node#set the dummy tail node

    def remove(self,node:DoublyListNode):
        node.prev.next=node.next
        node.next.prev=node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    LRU=LRUCache(2)
    LRU.put(1,1)
    LRU.put(2,2)
    LRU.get(1)
    LRU.put(3, 3)
    LRU.get(2)
    LRU.put(4, 4)
    LRU.get(1)
    LRU.get(3)
    LRU.get(4)