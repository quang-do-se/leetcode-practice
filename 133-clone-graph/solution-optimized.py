
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
                
        stack = [node]
        visited = {node.val: Node(node.val)}
        
        while stack: 
            current_node = stack.pop()
            
            for neighbor in current_node.neighbors:
                if neighbor.val not in visited:
                    cloned_neighbor = Node(neighbor.val)
                    visited[neighbor.val] = cloned_neighbor
                    stack.append(neighbor)
                    
                cloned_neighbor = visited.get(neighbor.val)
                visited[current_node.val].neighbors.append(cloned_neighbor)                    

        return visited[node.val]



        

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node0.neighbors = [node1]
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]

sol = Solution()
print(sol.cloneGraph(node0))
