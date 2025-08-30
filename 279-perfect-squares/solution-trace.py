from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        perfect_square_numbers = set()

        i = 1
        square_number = i * i
        while square_number <= n:
            perfect_square_numbers.add(square_number)            
            i += 1
            square_number = i * i

        queue = deque([(0, 0, [0])])
        visited = set([(0, 0)])

        while queue:
            size_at_current_level = len(queue)

            for _ in range(size_at_current_level):
                
                sum, steps, trace = queue.popleft()

                if sum == n:
                    print(trace)
                    return steps
                
                for square_number in perfect_square_numbers:
                    new_sum = [sum + square_number, steps + 1]
                    new_trace = trace + [square_number]
                    
                    new_sum_with_trace = tuple(new_sum + [new_trace])
                    new_sum = tuple(new_sum)
                    
                    if new_sum not in visited:
                        queue.append(new_sum_with_trace)
                        visited.add(new_sum)
            
        return -1


sol = Solution()
print(sol.numSquares(1) == 1)
print(sol.numSquares(2) == 2)
print(sol.numSquares(3) == 3)
print(sol.numSquares(36) == 1)
print(sol.numSquares(12) == 3)
print(sol.numSquares(13) == 2)
print(sol.numSquares(9999) == 4)
print(sol.numSquares(10 ** 4) == 1)

