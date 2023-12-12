
row = 3
col = 3
grid = []
for i in range(row):
    grid.append([None] * col)


# for i in range(row):
#     grid[i][0]='x'
#
# for p in range(row):
#     try:
#         grid[p].index(None)
#     except ValueError:
#         print("You win")
#         break


# for k in range(col):
#     column = [row[k] for row in grid]
#     try:
#         column.index(None)
#     except ValueError:
#         print("You win")
#         break

# diag=[]
# for d in range(row):
#         diag.append(grid[d][d])
# try:
#     diag.index(None)
# except ValueError:
#     print("You win")

grid[0][2]=2
grid[1][1]=2
grid[2][0]=2

# rdiag=[]
# for d in range(row):
#     rdiag.append(grid[d][row-1-d])
#
# print(rdiag)










#
# def check_the_win(self, grid) -> bool:
#     row = 3
#     col = 3
#
#     # проверяем строки
#     for p in range(row):
#         try:
#             grid[p].index(None)
#         except ValueError:
#             print("You win")
#             print(f'строка {p} заполнена {self.sign}')
#             return True
#
#     # проверяем столбцы
#     for k in range(col):
#         column = [row[k] for row in grid]
#         try:
#             column.index(None)
#         except ValueError:
#             print("You win")
#             print(f'столбец {k} заполнен {self.sign}')
#             return True
#
#     #     проверяем главную диагональ
#     diag = []
#     for d in range(row):
#         diag.append(grid[d][d])
#     try:
#         diag.index(None)
#     except ValueError:
#         print("You win")
#         print(f' главная диагональ заполнена {self.sign}')
#         return True
#
#     #     проверяем побочную диагональ
#     rdiag = []
#     for d in range(row):
#         rdiag.append(grid[d][row - 1 - d])
#     try:
#         rdiag.index(None)
#     except ValueError:
#         print("You win")
#         print(f'побочная диагональ заполнена {self.sign}')
#         return True
