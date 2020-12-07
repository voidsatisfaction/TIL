import random

class RandomizedSet:
    def __init__(self):
        self._value_set = {}
        self._value_list = []
        

    def insert(self, val: int) -> bool:
        if val in self._value_set:
            return False

        self._value_list.append(val)
        self._value_set[val] = len(self._value_list)-1

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self._value_set:
            return False

        if len(self._value_list) == 1:
            self._value_list.pop()
        else:
            last_val, val_index = self._value_list[-1], self._value_set[val]
            self._value_list[val_index], self._value_set[last_val] = last_val, val_index
            self._value_list.pop()

        del self._value_set[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self._value_list)
        

if __name__ == '__main__':
    rs = RandomizedSet()

    rs.insert(0)
    rs.insert(1)
    rs.remove(0)
    rs.insert(2)
    rs.remove(1)

    print(rs._value_set, rs._value_list)

    rs.remove(2)

    print(rs._value_set, rs._value_list)