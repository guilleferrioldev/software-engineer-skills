from typing import Tuple, List, Self, Optional

class Node:
    """Node implementation"""
    def __init__(self, point: Tuple[int, int], left: Optional[Self] = None, 
                 right: Optional[Self] = None, axis: int = None):
        self.point = point 
        self.left = left  
        self.right = right 
        self.axis = axis  

class KDTree:
    """KD Tree implementation"""
    def __init__(self, points: List[Tuple[int, int]]) -> None:
        self.root = self._build_tree(points)

    def _build_tree(self, points: Tuple[int, int], depth: int = 0) -> Optional[Node]:
        """Auxiliar method to build the tree recursively"""
        if not points:
            return None

        k = len(points[0])  
        axis = depth % k  

        points.sort(key = lambda point: point[axis])
        median = len(points) // 2

        return Node(
            points[median],
            self._build_tree(points[:median], depth + 1),
            self._build_tree(points[median + 1:], depth + 1),
            axis
        )
        
    def insert(self, point: Tuple[int, int]) -> None:
        """Method to insert a point"""
        def recursive_insert(node: Node, depth: int) -> Node:
            if not node:
                return Node(point, axis = depth % len(point))

            axis = node.axis
            if point[axis] < node.point[axis]:
                node.left = recursive_insert(node.left, depth + 1)
            else:
                node.right = recursive_insert(node.right, depth + 1)

            return node

        self.root = recursive_insert(self.root, 0)

    def nearest_neighbor(self, target: Tuple[int, int]) -> Tuple[int, int]:
        """Method to find the nearest neighbor"""
        best = None
        best_dist = float("inf")

        def recursive_search(node: Node) -> None:
            nonlocal best, best_dist
            if not node:
                return

            # Calculate distance to target point
            dist = sum((a - b) ** 2 for a, b in zip(target, node.point))
            if dist < best_dist:
                best = node.point
                best_dist = dist

            if target[node.axis] < node.point[node.axis]:
                recursive_search(node.left)
                if target[node.axis] + best_dist >= node.point[node.axis]:
                    recursive_search(node.right)
            else:
                recursive_search(node.right)
                if target[node.axis] - best_dist <= node.point[node.axis]:
                    recursive_search(node.left)

        recursive_search(self.root)
        return best
    
    def delete(self, point_to_delete: Tuple[int, int]) -> None:
        """Method to delete a point"""
        def recursive_delete(node: Node, point: Tuple[int, int], depth: int) -> Node:
            if node is None:
                return None

            axis = depth % len(point)
            if point[axis] < node.point[axis]:
                node.left = recursive_delete(node.left, point, depth + 1)
            elif point[axis] > node.point[axis]:
                node.right = recursive_delete(node.right, point, depth + 1)
            else:
                if node.point == point:
                    if node.right:
                        min_point = find_min(node.right, depth % len(point))
                        node.point = min_point
                        node.right = recursive_delete(node.right, min_point, depth + 1)
                    elif node.left:
                        min_point = find_min(node.left, depth % len(point))
                        node.point = min_point
                        node.left = recursive_delete(node.left, min_point, depth + 1)
                    else:
                        return None  
                else:
                    node.left = recursive_delete(node.left, point, depth + 1)

            return node

        def find_min(node: Node, axis: int) -> Tuple[int, int]:
            while node.left:
                node = node.left
            return node.point

        self.root = recursive_delete(self.root, point_to_delete, 0)
        
    def __repr__(self) -> str:
        result = []
        def in_order_traversal(node, lst):
            if node:
                in_order_traversal(node.left, lst)
                lst.append(node.point)
                in_order_traversal(node.right, lst)

        in_order_traversal(self.root, result)
        return f"{result}"