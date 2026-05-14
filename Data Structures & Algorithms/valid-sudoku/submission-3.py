class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash, colHash = defaultdict(set), defaultdict(set)
        matrixHash = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                mat = (i // 3, j // 3)

                if board[i][j] in rowHash[i] or board[i][j] in colHash[j] or board[i][j] in matrixHash[mat]:
                    return False

                rowHash[i].add(board[i][j])
                colHash[j].add(board[i][j])
                matrixHash[mat].add(board[i][j])

        return True