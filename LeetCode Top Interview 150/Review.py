class DoublyListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dict={}# to store key->DoublyListNode
        self.head=DoublyListNode(-1,-1)
        self.tail=DoublyListNode(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node=self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.dict:# renew it
            nodeToDelete=self.dict[key]
            self.remove(nodeToDelete)
        nodeToAdd=DoublyListNode(key,value)
        self.add(nodeToAdd)
        self.dict[key]=nodeToAdd

        #check capacity
        if len(self.dict)>self.capacity:
            nodeToDelete=self.head.next
            self.remove(nodeToDelete)
            del self.dict[nodeToDelete.key]

    def add(self, node):
        prev=self.tail.prev# the real tail element in LRU
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node

    def remove(self, node):
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