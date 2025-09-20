from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        stack = [0]
        visited = set([0])

        while stack:
            current_room = stack.pop()
            keys = rooms[current_room]

            for key in keys:
                if key not in visited:
                    stack.append(key)
                    visited.add(key)
        
        return len(visited) == n

sol = Solution()
rooms = [[1],[2],[3],[]]

print(sol.canVisitAllRooms([[1],[2],[3],[]]) == True)
print(sol.canVisitAllRooms([[1],[],[3],[2]]) == False)
print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False)
print(sol.canVisitAllRooms([[2],[],[1]]) == True)
