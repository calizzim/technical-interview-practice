from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layers = n // 2
        for layer in range(layers):
            layerDim = n - 2 * layer
            for index in range(layerDim-1):
                coords = [
                    [layer, layer + index],
                    [layer + index, layer + layerDim -1],
         [layer + layerDim - 1, layer + layerDim - index - 1],
                    [layer + layerDim - index - 1, layer],
                ]
                temp = matrix[coords[1][0]][coords[1][1]]
                matrix[coords[1][0]][coords[1][1]] = matrix[coords[0][0]][coords[0][1]]
                matrix[coords[2][0]][coords[2][1]], temp = temp, matrix[coords[2][0]][coords[2][1]]
                matrix[coords[3][0]][coords[3][1]], temp = temp, matrix[coords[3][0]][coords[3][1]]
                matrix[coords[0][0]][coords[0][1]], temp = temp, matrix[coords[0][0]][coords[0][1]]           
        
s = Solution()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s.rotate(matrix)
print(matrix)