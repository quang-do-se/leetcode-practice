
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
        visited = set([node])
        cloned_nodes = {node.val: Node(node.val)}
        
        while stack: 
            current_node = stack.pop()

            cloned_nodes[current_node.val].neighbors = []
            
            for neighbor in current_node.neighbors:
                if neighbor.val in cloned_nodes:
                    cloned_neighbor = cloned_nodes.get(neighbor.val)
                else:
                    cloned_neighbor = Node(neighbor.val)
                    cloned_nodes[cloned_neighbor.val] = cloned_neighbor

                cloned_nodes[current_node.val].neighbors.append(cloned_neighbor)

                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return cloned_nodes[node.val]



        

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
