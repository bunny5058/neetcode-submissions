class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in matrix[i]:
                if target == j:
                    return True
                else:
                    pass
        return False