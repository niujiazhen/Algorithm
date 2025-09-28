class DoublyListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic = {}
        self.head = DoublyListNode(-1, -1)
        self.tail = DoublyListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node=self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node=self.dic[key]
            self.remove(old_node)

        new_node=DoublyListNode(key,value)
        self.add(new_node)
        self.dic[key]=new_node

        if len(self.dic)>self.capacity:
            deleteNode=self.head.next
            self.remove(deleteNode)
            del self.dic[deleteNode.key]

    def add(self, node):
        previous_end=self.tail.prev#the real tail element
        previous_end.next=node#add the node to the tail
        node.prev=previous_end
        node.next=self.tail
        self.tail.prev=node#set the node to be the real tail element

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