import random

class RandomizedSet:

    def __init__(self):
        self.set = []

    def insert(self, val: int) -> bool:
        len_set = len(self.set)
        if len_set == 0:
            self.set.append(val)
            return True
        else:
            for i in range(len_set):
                if self.set[i] == val:
                    return False

            self.set.append(val)
            return True

    def remove(self, val: int) -> bool:
        len_set = len(self.set)
        if len_set == 0:
            return False
        else:
            for i in range(len_set):
                if self.set[i] == val:
                    self.set.remove(val)
                    return True
            return False

    def getRandom(self) -> int:
        if len(self.set) == 0:
            return False
        else:
            return random.choice(self.set)


if __name__ == "__main__":
    val = 1
    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    param_1 = obj.insert(0)
    param_1 = obj.insert(2)
    param_1 = obj.insert(1)
    param_1 = obj.insert(1)
    param_1 = obj.insert(1)
    param_2 = obj.remove(val)
    param_3 = obj.getRandom()