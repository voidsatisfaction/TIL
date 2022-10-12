from typing import List

class Trie:
    class TrieNode:
        def __init__(self, val: str):
            self._val = val
            self._is_word = False
            self._children = {}

        def get_word(self) -> str:
            return self._val

        def is_word(self) -> bool:
            return self._is_word

    def __init__(self):
        self._root = self.TrieNode('')

    def add_word(self, word: str) -> None:
        last_node = self._root
        for c in word:
            if c in last_node._children:
                last_node = last_node._children[c]
                continue
            last_node._children[c] = new_node = self.TrieNode(last_node._val + c)
            last_node = new_node

        last_node._is_word = True

    def get_root_node(self) -> TrieNode:
        return self._root

    def get_child_node(self, current_node: TrieNode, c: str) -> TrieNode:
        if c in current_node._children:
            return current_node._children[c]

        return None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i: int, j: int, N: int, M: int, board, visited: List[List[bool]], answer: List[str], trie: Trie, current_node: Trie.TrieNode) -> None:
            direction_list = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for (yy, xx) in direction_list:
                next_i, next_j = i + yy, j + xx

                if next_i >= N or next_i < 0 or next_j >= M or next_j < 0 or visited[next_i][next_j] is True:
                    continue
                
                next_c = board[next_i][next_j]
                next_trie_node = trie.get_child_node(current_node, next_c)

                if next_trie_node is not None:
                    if next_trie_node.is_word():
                        answer.add(next_trie_node.get_word())

                    visited[next_i][next_j] = True
                    dfs(next_i, next_j, N, M, board, visited, answer, trie, next_trie_node)
                    visited[next_i][next_j] = False

        trie = Trie()

        for word in words:
            trie.add_word(word)

        N, M = len(board), len(board[0])
        visited = [[False for _ in range(M)] for _ in range(N)]
        answer = set()

        for i in range(N):
            for j in range(M):
                trie_root_node = trie.get_root_node()

                c = board[i][j]
                child_node = trie.get_child_node(trie_root_node, c)

                visited[i][j] = True

                if child_node is not None:
                    if child_node.is_word():
                        answer.add(child_node.get_word())

                    dfs(i, j, N, M, board, visited, answer, trie, child_node)

                visited[i][j] = False

        return list(answer)


if __name__ == '__main__':
    s = Solution()

    print(s.findWords([
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ], ['oath', 'pea', 'eat', 'rain']))

    print(s.findWords([
        ['o']
    ], []))

    print(s.findWords([
        ['o']
    ], ['o']))

    print(s.findWords([
        ['o']
    ], ['l']))

    print(s.findWords([
        ['a', 'a']
    ], ['a']))