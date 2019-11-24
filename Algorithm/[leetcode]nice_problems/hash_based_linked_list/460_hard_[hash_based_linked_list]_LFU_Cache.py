import collections

class Node:
  def __init__(self, key: int, value: int):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None
    self.freq = 1

class NodeBasedLinkedList:
  def __init__(self):
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.linkedList = {}

  def addToFrontList(self, node: Node) -> None:
    beforeNextHeadNode = self.head.next

    self.head.next = node
    beforeNextHeadNode.prev = node
    node.prev = self.head
    node.next = beforeNextHeadNode

    self.linkedList[node.key] = node

  def removeFromList(self, node: Node) -> None:
    targetNode = self.linkedList[node.key]
    targetNodePrev = targetNode.prev
    targetNodeNext = targetNode.next

    targetNodePrev.next = targetNodeNext
    targetNodeNext.prev = targetNodePrev
    del self.linkedList[node.key]

class LFUCache:
  def __init__(self, capacity: int):
    self._capacity = capacity
    self._freqs = collections.defaultdict(NodeBasedLinkedList)
    self._nodes = {}
    self._minFreq = 1
    self._nodeNum = 0

  def get(self, key: int) -> int:
    if self._capacity == 0:
      return -1
      
    if key in self._nodes:
      node = self._nodes[key]
      minFreq, nodeFreq, nextNodeFreq = self._minFreq, node.freq, node.freq+1

      self._freqs[nodeFreq].removeFromList(node)
      node.freq = nextNodeFreq
      self._freqs[nextNodeFreq].addToFrontList(node)

      if nodeFreq == minFreq and len(self._freqs[minFreq].linkedList) == 0:
        self._minFreq += 1
      
      return node.value

    return -1

  def put(self, key: int, value: int) -> None:
    if self._capacity == 0:
      return
    nextFreq = 1
    minFreq = self._minFreq
    node = Node(key, value)
    if key in self._nodes:
      node = self._nodes[key]
      node.value = value

      nextFreq = node.freq + 1
      self._freqs[node.freq].removeFromList(node)
    else:
      self._nodeNum += 1

    if self._nodeNum > self._capacity:
      leastUsedOutdatedNode = self._freqs[minFreq].tail.prev

      self._freqs[minFreq].removeFromList(leastUsedOutdatedNode)
      del self._nodes[leastUsedOutdatedNode.key]
      self._nodeNum -= 1
    
    node.freq = nextFreq
    self._freqs[nextFreq].addToFrontList(node)
    self._freqs[nextFreq].linkedList[node.key] = node
    self._nodes[node.key] = node

    if len(self._freqs[minFreq].linkedList) == 0 or nextFreq < minFreq:
      self._minFreq = nextFreq

# cache = LFUCache(2)

# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))       # returns 1
# cache.put(3, 3)    # evicts key 2
# print(cache.get(2))       # returns -1 (not found)
# print(cache.get(3))       # returns 3.
# cache.put(4, 4)    # evicts key 1.
# print(cache.get(1))       # returns -1 (not found)
# print(cache.get(3))       # returns 3
# print(cache.get(4))       # returns 4

cache = LFUCache(3)

cache.put(2, 2)
cache.put(1, 1)
print(cache.get(2))       # returns 1
print(cache.get(1))       # returns 1
print(cache.get(2))       # returns 1
cache.put(3, 3)    # evicts key 2
print(cache._minFreq, cache._nodes, cache._freqs)
cache.put(4, 4)    # evicts key 1.
print(cache._minFreq, cache._nodes, cache._freqs)
print(cache.get(3))       # returns 3.
print(cache.get(2))       # returns -1 (not found)
print(cache.get(1))       # returns -1 (not found)
print(cache.get(4))       # returns 4