from typing import List

# Backtracking
# with additional visited
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(y, x, next_index, visited) -> bool:
            if next_index == len(word):
                return True

            positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            result = False

            for position in positions:
                neighbor_y, neighbor_x = position[0]+y, position[1]+x

                if neighbor_y < 0 or neighbor_y > total_row-1 or neighbor_x < 0 or neighbor_x > total_column-1 or visited[neighbor_y][neighbor_x] or board[neighbor_y][neighbor_x] != word[next_index]:
                    continue
                
                visited[neighbor_y][neighbor_x] = True
                result = result or dfs(neighbor_y, neighbor_x, next_index+1, visited)
                visited[neighbor_y][neighbor_x] = False

            return result

        total_row, total_column = len(board), len(board[0])

        visited = [ [ False for _ in range(total_column) ] for _ in range(total_row) ]

        answer = False
        for row in range(total_row):
            for column in range(total_column):
                if board[row][column] == word[0]:
                    visited[row][column] = True
                    answer = answer or dfs(row, column, 1, visited)
                    visited[row][column] = False

        return answer

# Backtracking
# without additional visited

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(y, x, next_index) -> bool:
            if next_index == len(word):
                return True

            positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            result = False

            for position in positions:
                neighbor_y, neighbor_x = position[0]+y, position[1]+x

                if neighbor_y < 0 or neighbor_y > total_row-1 or neighbor_x < 0 or neighbor_x > total_column-1 or board[neighbor_y][neighbor_x] != word[next_index]:
                    continue
                
                board[neighbor_y][neighbor_x] = '$'
                result = result or dfs(neighbor_y, neighbor_x, next_index+1)
                board[neighbor_y][neighbor_x] = word[next_index]

            return result

        total_row, total_column = len(board), len(board[0])

        visited = [ [ False for _ in range(total_column) ] for _ in range(total_row) ]

        for row in range(total_row):
            for column in range(total_column):
                if board[row][column] == word[0]:
                    board[row][column] = '$'

                    if dfs(row, column, 1):
                        return True

                    board[row][column] = word[0]

        return False

if __name__ == '__main__':
    print(Solution().exist([
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ], 'ABCCED'))

    print(Solution().exist([
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ], 'SEE'))

    print(Solution().exist([
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ], 'ABCB'))