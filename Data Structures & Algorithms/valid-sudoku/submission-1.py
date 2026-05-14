class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash, colHash = [set() for _ in range(9)], [set() for _ in range(9)]
        matrixHash = defaultdict(set)

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == ".":
                    continue
                mat = (i // 3, j // 3)
                if c in rowHash[i] or c in colHash[j] or c in matrixHash[mat]:
                    return False
                rowHash[i].add(c)
                colHash[j].add(c)
                matrixHash[mat].add(c)
        
        return True