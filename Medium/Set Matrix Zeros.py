class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])
        zero_indices = {
            "row": set(),
            "col": set()
        }
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_indices["row"].add(i)
                    zero_indices["col"].add(j)
        for i in zero_indices["row"]:
            matrix[i] = [0] * m
        for j in zero_indices["col"]:
            for i in range(n):
                matrix[i][j] = 0