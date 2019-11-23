from typing import List, Dict

# simpler solution

class Node:
  def __init__(self, key: int, value: int):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None

  def setPrev(self, prevNode) -> None:
    self.prev = prevNode

  def setNext(self, nextNode) -> None:
    self.next = nextNode

class LRUCache:
  def __init__(self, capacity: int):
    self._capacity = capacity
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    self.head.setNext(self.tail)
    self.tail.setPrev(self.head)
    self.hashedLinkedList = {}

  def get(self, key: int) -> int:
    if key in self.hashedLinkedList:
      node = self.hashedLinkedList[key]
      self._removeLink(node)
      self._addLinkOnFront(node)
      return node.value
    return -1

  def put(self, key: int, value: int) -> None:
    newNode = Node(key, value)
    if key in self.hashedLinkedList:
      existedNode = self.hashedLinkedList[key]
      self._removeLink(existedNode)

    self._addLinkOnFront(newNode)
    self.hashedLinkedList[key] = newNode

    if len(self.hashedLinkedList) > self._capacity:
      n = self.tail.prev
      self._removeLink(n)
      del self.hashedLinkedList[n.key]


  def _removeLink(self, node: Node) -> None:
    prevNode = node.prev
    nextNode = node.next

    prevNode.setNext(nextNode)
    nextNode.setPrev(prevNode)

  def _addLinkOnFront(self, node: Node) -> None:
    headNode = self.head
    beforeHeadNextNode = self.head.next

    headNode.setNext(node)
    beforeHeadNextNode.setPrev(node)
    node.setPrev(headNode)
    node.setNext(beforeHeadNextNode)

# my first solution

class KeyValueStorage:
  def __init__(self):
    self.keyValueStorage = {}

  def get(self, key: int) -> int:
    return self.keyValueStorage.get(key)

  def put(self, key: int, value: int) -> None:
    self.keyValueStorage[key] = value

  def remove(self, key: int) -> None:
    self.keyValueStorage.pop(key, None)

class LatestUsedKeyHistory:
  def __init__(self, capacity: int, keyValueStorage: KeyValueStorage):
    self.latestUsedKey = None
    self.lastUsedKey = None
    self.historyNum = 0
    self.historyList = {}
    self._capacity = capacity
    self._keyValueStorage = keyValueStorage

  def latestUsedKey(self) -> int:
    return self.latestUsedKey

  def lastUsedKey(self) -> int:
    return self.lastUsedKey

  def historyNum(self) -> int:
    return self.historyNum

  def addNewHistory(self, key: int) -> None:
    if self.historyNum == 0:
      self.latestUsedKey = key
      self.lastUsedKey = key
      self.historyNum = 1
      self.historyList[key] = { "prev": -1, "next": -1 }
    elif self.latestUsedKey == key:
      pass
    elif self.lastUsedKey == key:
      beforeLatestUsedKey = self.latestUsedKey
      prevKey = self.historyList.get(key).get("prev")
      self.latestUsedKey = key
      self.lastUsedKey = prevKey
      self.historyList[key] = { "prev": -1, "next": beforeLatestUsedKey }
      self.historyList[beforeLatestUsedKey]["prev"] = key
      self.historyList[prevKey]["next"] = -1
    elif self.historyList.get(key) is not None:
      beforeLatestUsedKey = self.latestUsedKey
      prevKey = self.historyList.get(key).get("prev")
      nextKey = self.historyList.get(key).get("next")

      self.latestUsedKey = key
      self.historyList[key] = { "prev": -1, "next": beforeLatestUsedKey }
      self.historyList[beforeLatestUsedKey]["prev"] = key
      self.historyList[prevKey]["next"] = nextKey
      self.historyList[nextKey]["prev"] = prevKey
    else:
      beforeLatestUsedKey = self.latestUsedKey
      beforeLastUsedKey = self.lastUsedKey

      self.latestUsedKey = key
      self.historyNum += 1
      self.historyList[key] = { "prev": -1, "next": beforeLatestUsedKey }
      self.historyList[beforeLatestUsedKey]["prev"] = key

      if self.historyNum > self._capacity:
        if self._capacity == 1:
          self.lastUsedKey = key
          self.historyList[key] = { "prev": -1, "next": -1 }
        else:
          prevBeforeLastUsedKey = self.historyList[beforeLastUsedKey]["prev"]
          self.lastUsedKey = prevBeforeLastUsedKey
          self.historyList[prevBeforeLastUsedKey]["next"] = -1
        self.historyNum -= 1
        self.historyList.pop(beforeLastUsedKey, None)

        self._keyValueStorage.remove(beforeLastUsedKey)

class LRUCache:
  def __init__(self, capacity: int):
    self.keyValueStorage = KeyValueStorage()
    self.latestUsedKeyHistory = LatestUsedKeyHistory(capacity, self.keyValueStorage)

  def get(self, key: int) -> int:
    mayBeValue = self.keyValueStorage.get(key)
    if mayBeValue is not None:
      self.latestUsedKeyHistory.addNewHistory(key)
      return mayBeValue
    return -1

  def put(self, key: int, value: int) -> None:
    self.keyValueStorage.put(key, value)
    self.latestUsedKeyHistory.addNewHistory(key)

lruc = LRUCache(2)

lruc.put(1, 1)
lruc.put(2, 2)
lruc.put(1, 3)
print(lruc.get(1))
lruc.put(1, 4)
print(lruc.get(1))
lruc.put(3, 3) 
print(lruc.get(2))
lruc.put(4, 4)    
print(lruc.get(1))
print(lruc.get(3))
print(lruc.get(4))