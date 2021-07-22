def check_neighbours(row, col, brd, vis):
    vis[row][col] = True
    if row > 0 and brd[row - 1][col] == "1" and vis[row - 1][col] is False:
        check_neighbours(row - 1, col, brd, vis)
    if col > 0 and brd[row][col - 1] == "1" and vis[row][col - 1] is False:
        check_neighbours(row, col - 1, brd, vis)
    if row < len(brd) - 1 and brd[row + 1][col] == "1" and vis[row + 1][col] is False:
        check_neighbours(row + 1, col, brd, vis)
    if col < len(brd[0]) - 1 and brd[row][col + 1] == "1" and vis[row][col + 1] is False:
        check_neighbours(row, col + 1, brd, vis)


row_cnt = int(input())
board = []
blocks = 0
for row_index in range(row_cnt):
    one_row = input().split()
    board.append(one_row)
visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
for idx_row, one_row in enumerate(board):
    for idx_col, vlu in enumerate(one_row):
        if vlu == "1" and visited[idx_row][idx_col] is False:
            check_neighbours(idx_row, idx_col, board, visited)
            blocks += 1
print(blocks)
