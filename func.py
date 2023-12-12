class Game():
    """Выбирите, за кого будите играть: x или o
    метод turn - сообщите координаты ячейки, в которой хотите поставить символ"""

    def __init__(self, sign='x'):
        # Если выбран х - то ходит первым
        self.sign = sign
        self.grid = self.create_a_grid()

    def create_a_grid(self) -> list:
        '''Создаём сетку для заполнения'''
        row = 3
        col = 3
        grid = []
        for i in range(row):
            grid.append([None] * col)
        return grid

    def check_is_empty(self, grid, i, j) -> list:
        '''Проверяет, свободна ли ячейка, просит ввести новые координаты для того, чтобы выпонить ход'''
        while grid[i][j] != None:
            print('ячейка уже занята')
            print('выберите пустую ячейку')
            i = int(input('i= '))
            j = int(input('j= '))
        return i, j
    def check_the_win(self, func):
        def wrapper(*args, **kwargs)->bool:

            row = 3
            col = 3
            grid=func(*args, **kwargs)
            # проверяем строки
            for p in range(row):
                try:
                    grid[p].index(None)
                except ValueError:
                    print("You win")
                    print(f'строка {p} заполнена {self.sign}')
                    return True

            # проверяем столбцы
            for k in range(col):
                column = [row[k] for row in grid]
                try:
                    column.index(None)
                except ValueError:
                    print("You win")
                    print(f'столбец {k} заполнен {self.sign}')
                    return True

            #     проверяем главную диагональ
            diag = []
            for d in range(row):
                diag.append(grid[d][d])
            try:
                diag.index(None)
            except ValueError:
                print("You win")
                print(f' главная диагональ заполнена {self.sign}')
                return True

            #     проверяем побочную диагональ
            rdiag = []
            for d in range(row):
                rdiag.append(grid[d][row - 1 - d])
            try:
                rdiag.index(None)
            except ValueError:
                print("You win")
                print(f'побочная диагональ заполнена {self.sign}')
                return True
        return wrapper

    @check_the_win
    def turn(self, i=0, j=0):
        '''Ход человека, принимает координаты ячейки'''
        grid = self.grid
        # проверяем, не занята ли ячейка
        indexes = self.check_is_empty(grid=grid, i=i, j=j)
        i = indexes[0]
        j = indexes[1]
        # заполняем поле
        grid[i][j] = self.sign

        return grid


game = Game('x')
print(game.turn(0, 0))
print(game.turn(1, 1))
print(game.turn(2, 2))

