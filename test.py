from func import player, Game

x= player('x')
o= player('o')

f=Game()
f.play(x,0,0)
f.play(o,0,1)
f.play(x,1,0)
f.play(o,0,2)
f.play(x,2,0)



#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     def __repr__(self):
#         return f'{self.name} {self.surname}'
#     @property
#     def full_name(self):
#         return self.name + ' ' + self.surname
#
# A=Person('F', 'K')
# print(A.full_name)


#
# def create_a_grid() -> list:
#     '''Создаём сетку для заполнения'''
#     row = 3
#     col = 3
#     grid = []
#     for i in range(row):
#         grid.append([None] * col)
#     return grid
# print(len(create_a_grid()[0]))



# row = 3
# col = 3
# grid = []
# for i in range(row):
#     grid.append([None] * col)


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

# grid[0][2]=2
# grid[1][1]=2
# grid[2][0]=2

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
