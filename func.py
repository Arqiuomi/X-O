class player():
    """Выбирите, за кого будите играть"""

    def __init__(self, sign='x'):
        # Если выбран х - то ходит первым
        self.sign = sign


class Game():
    """Выбирите, за кого будите играть в классе п: x или o
    метод turn - сообщите координаты ячейки, в которой хотите поставить символ"""

    def __init__(self):
        # Если выбран х - то ходит первым
        self.grid = self.create_a_grid()
        self.length = len(self.grid[0])

    def create_a_grid(self) -> list:
        '''Создаём сетку для заполнения'''
        row = 3
        col = 3
        grid = []
        for i in range(row):
            grid.append([None] * col)
        return grid

    def check_is_empty(self, i, j) -> list:
        '''Проверяет, свободна ли ячейка'''
        if self.grid[i][j] != None:
            print('ячейка уже занята')
            print('выберите пустую ячейку')
        else:
            return i, j

    def turn(self, player, i=0, j=0):
        '''Ход человека, принимает координаты ячейки'''
        # проверяем, не занята ли ячейка
        indexes = self.check_is_empty(i=i, j=j)
        try:
            i = indexes[0]
            j = indexes[1]
            # заполняем поле
            self.grid[i][j] = player
            return self.grid
        except ValueError:
            return self.grid

    def check_rows(self, player) -> bool:
        """ проверяем строки"""
        for p in range(self.length):
            try:
                self.grid[p].index(None)
            except ValueError:
                if self.grid[p].count(player) == 3:
                    print("You win")
                    print(f'строка {p} заполнена {player}')
                    return True

    def check_cols(self, player) -> bool:
        ''' проверяем столбцы'''
        for k in range(self.length):
            # Обращение к столбцам
            column = [row[k] for row in self.grid]
            try:
                column.index(None)
            except ValueError:
                if column.count(player) == 3:
                    print("You win")
                    print(f'столбец {k} заполнен {player}')
                    return True

    def check_diag(self, player) -> bool:
        '''проверяем главную диагональ'''
        diag = []
        for d in range(self.length):
            diag.append(self.grid[d][d])
        try:
            diag.index(None)
        except ValueError:
            if diag.count(player) == 3:
                print("You win")
                # print(f' главная диагональ заполнена {self.sign}')
                return True

    def check_cross_diag(self, player) -> bool:
        '''проверяем побочную диагональ'''
        rdiag = []
        for d in range(self.length):
            rdiag.append(self.grid[d][self.length - 1 - d])
        try:
            rdiag.index(None)
        except ValueError:
            if rdiag.count(player)==3:
                print("You win")
                # print(f'побочная диагональ заполнена {self.sign}')
                return True

    def check_the_win(self, player) -> None:

        self.check_rows(player)
        self.check_cols(player)
        self.check_diag(player)
        self.check_cross_diag(player)

    def play(self, player, i=0, j=0):
        '''Основной ход игры'''
        self.turn(player.sign, i, j)
        self.check_the_win(player.sign)
        print(self.grid)
