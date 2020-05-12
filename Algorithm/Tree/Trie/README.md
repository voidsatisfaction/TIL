# Trie (Prefix tree, digital tree)

- 의문
- 개요
  - 정의
  - 특징
  - 응용
  - 참고) radix tree
- 구현

## 의문

## 개요

Trie example

![](./images/trie_example1.png)

### 정의

- search tree인데, order가 존재하고, dynamic set이나 associative array를 저장하는데 사용되고, 키가 주로 string이다

### 특징

- 키의 값은 노드에 연관되는 것이 아니고, 트리 전반에 분포됨
- 특정 노드의 자손들은 노드에 연관되는 동일 prefix를 갖음
  - root는 empty string
- 장점
  - hash table에 비해서 다음과 같은 장점을 갖음
    - collision을 갖는 해시 트리(`O(max(N, m))` `m`은 왜냐하면, hash를 evaluate하는데에 걸리는 시간) 보다 효율적(`O(m)`)
    - 키 collision이 없음
    - 키가 추가돼도 hash function같은 것들이 필요 없음
    - 키에 의한 알파벳 ordering을 제공할 수 있음

### 응용

- Autocomplete
- Spell checker
- IP routing
  - Longest prefix matching
- Solving word games

### 참고) radix tree

- 정의
  - space-optimized trie
    - child가 하나인 각각의 노드는 부모노드와 함게 결합됨

## 구현

- ApI
  - Create
  - Read
  - *Update*
  - *Delete*

```py
class Node:
    def __init__(self, val, is_word=False):
        self.val = val
        self.children = {}
        self.is_word = is_word

class Trie:

    def __init__(self):
        self.children = {}


    def insert(self, word: str) -> None:
        last_node = self
        for c in word:
            if not last_node.children.get(c):
                last_node.children[c] = Node(c)

            last_node = last_node.children[c]

        last_node.is_word = True


    def search(self, word: str) -> bool:
        last_node = self._search_prefix(word)

        return last_node is not None and last_node.is_word


    def startsWith(self, prefix: str) -> bool:
        last_node = self._search_prefix(prefix)

        return last_node is not None

    def _search_prefix(self, prefix: str) -> bool:
        last_node = self
        for c in prefix:
            if not last_node.children.get(c):
                return None

            last_node = last_node.children[c]

        return last_node


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    trie = Trie();

    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True

    trie = Trie()

    trie.insert("a")
    assert trie.search("a") == True
    assert trie.startsWith("a") == True
```
