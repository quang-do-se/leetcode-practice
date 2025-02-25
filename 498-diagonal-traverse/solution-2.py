from typing import List


class Solution:
    # One of the fastest solution on LeetCode, it processes diagonals in pair
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1:
            return mat[0]
        
        array = []
        row,col = len(mat),len(mat[0])
        i,j=0,0

        while 0<=i<row and 0<=j<col:
            while i>=0 and j<col:
                print(f"Add {i,j}")
                array.append(mat[i][j])
                i-=1
                j+=1
            i+=1
            if j == col:
                i+=1    
                j-=1

            print(i,j)
            print("Process the neighbor diagonal in reverse order")

            while i<row and j>=0:
                print(f"Add {i,j}")
                array.append(mat[i][j])
                j-=1
                i+=1
            j+=1
            if i == row:
                i-=1    
                j+=1
            print(i,j)

            print(f"Finish one loop: {array}")
            print()

        return array


sol = Solution()
print(sol.findDiagonalOrder([[1,2,3], [4,5,6], [7,8,9]]))