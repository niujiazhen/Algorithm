class DoublyLinkedList:
    def __init__(self, key: int, val: int, ):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None# help delete the node in O(1)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash={}# map key -> DoublyLinkedList

        # the real LinkedList is between dummyHead and dummyTail
        self.dummyHead=DoublyLinkedList(-1,-1)
        self.dummyTail=DoublyLinkedList(-1,-1)
        self.dummyHead.next=self.dummyTail
        self.dummyTail.prev=self.dummyHead

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node=self.hash[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # If key-value pair exist in List
        if key in self.hash:
            oldNode=self.hash[key]
            self.remove(oldNode)
            self.add(DoublyLinkedList(key,value)) # add the original node with new value to the tail of list
            return
        newNode=DoublyLinkedList(key,value)
        self.add(newNode)


        #check the capacity
        if len(self.hash)>self.capacity:
            # we have to remove the least used node
            leastUsedNode=self.dummyHead.next
            self.remove(leastUsedNode)
            del self.hash[leastUsedNode.key]


    def add(self, node: DoublyLinkedList):# add the node to the tail of DoublyLinkedList
        realTail=self.dummyTail.prev
        realTail.next=node
        node.prev=realTail
        node.next=self.dummyTail
        self.dummyTail.prev=node
        self.hash[node.key] = node


    def remove(self, node: DoublyLinkedList):
        node.prev.next=node.next
        node.next.prev=node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    lru=LRUCache()
