from typing import List

class Node:
    def __init__(self, value: int, is_leaf: bool, topLeft: int = None, topRight: int = None, 
                 bottomLeft: int = None, bottomRight: int = None) -> None:
        self.value = value
        self.is_leaf = is_leaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class QuadTree:
    def __init__(self, grid: List[List[int]]) -> None:
        self.tree = self._construct(grid)
    
    def _construct(self, grid: List[List[int]]) -> Node:
        def dfs(number: int, row: int, column: int):
            allSame = True
            for i in range(number):
                for j in range(number):
                    if grid[row][column] != grid[row + i][column + j]:
                        allSame = False
                        break
                
            if allSame:
                return Node(grid[row][column], True)
            
            number = number // 2
            topleft = dfs(number, row, column)
            topright = dfs(number, row, column + number)
            bottomleft = dfs(number, row + number, column)
            bottomright = dfs(number, row + number, column + number)
            return Node(0, False, topleft, topright, bottomleft, bottomright)
            
        return dfs(len(grid), 0, 0)