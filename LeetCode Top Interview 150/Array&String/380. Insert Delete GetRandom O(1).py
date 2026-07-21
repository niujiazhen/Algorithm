from random import choice


class RandomizedSet:
    # we need to make the following three function to be O(1)
    def __init__(self):
        self.dict={}# the time complexity of remove in a dictionary is O(1)
        self.list=[]# the time complexity of insert and getRandom in a list is O(1)

    def insert(self, val: int) -> bool:
        if val in self.dict:#already exist
            return False
        self.dict[val]=len(self.list) # record the index of the val in list
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # to make a remove to be O(1) in a list, we first swap the val element and the last element, then pop the last element, so the time complexity is O(1)
        lastElement=self.list[-1]
        removeIndex=self.dict[val]
        self.list[removeIndex]=lastElement
        self.dict[lastElement]=removeIndex

        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list)


if __name__ == '__main__':
    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    param_1 = obj.insert(val)
    param_2 = obj.remove(val)
    param_3 = obj.getRandom()