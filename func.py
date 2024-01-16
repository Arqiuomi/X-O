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
        '''Проверяет, свободна ли ячейка
        i: int
        j: int'''

        if self.grid[i][j] != None:
            print('ячейка уже занята')
            print('выберите пустую ячейку')
            raise IndexError
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
        return False

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
            return False

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
        return False

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
        return False
    def check_space(self):
        # for p in range(self.length):
        c=0
        for p in range(self.length):
            try:
                self.grid[p].index(None)
            except ValueError:
                c+=1
            if c==3:
                print("No space, the game has ended")
                return True
        return False

    def check_the_win(self, player) -> bool:
        return self.check_rows(player) or self.check_cols(player) or self.check_diag(player) or self.check_cross_diag(player)

    def change_player(self, player='o'):
        if player=='o':
            player=='x'
        elif player=='x':
            player=='o'

        if player=='x':
            return 'o'
        else:
            return 'x'

    def play(self, player, i=0, j=0):
        '''Основной ход игры'''
        while not self.check_the_win(player) or not self.check_space():
            try:
                move = list(map(int, input().split(' ')))
                self.turn(player, move[0], move[1])
            except IndexError:
                continue
            except Exception:
                continue
            self.check_the_win(player)
            self.check_space()
            print(self.grid)
            player = self.change_player(player)
