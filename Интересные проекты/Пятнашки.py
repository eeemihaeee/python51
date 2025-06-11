import random
import os
import subprocess
# Класс "Пятнашки".
class Fifteen:
    #Конструктор класса
    def __init__(self, size=4):
        #Инициализирует игру с заданным размером.
        self.size = size #Размер игрового поля (по умолчанию 4).
        self.tiles = list(range(1, size * size)) + [0]  # 0 представляет пустую клетку
        self.empty_tile_index = size * size - 1  # Индекс пустой клетки
        self.shuffle() #Перемешивание
    # Перемешивает плитки для начала новой игры.
    def shuffle(self, moves=1000):
        for i in range(moves):
            possible_moves = self.get_possible_moves()
            move = random.choice(possible_moves)
            self.move(move)
    #Возвращает список возможных перемещений (направлений: 'up', 'down', 'left', 'right').
    def get_possible_moves(self):
        row, col = divmod(self.empty_tile_index, self.size) #Строки, колонки
        possible_moves = [] #Возможные ходы
        if row > 0:
            possible_moves.append('u')
        if row < self.size - 1:
            possible_moves.append('d')
        if col > 0:
            possible_moves.append('l')
        if col < self.size - 1:
            possible_moves.append('r')
        return possible_moves
    #Перемещает плитку в заданном направлении, если это возможно.
    def move(self, direction):
        row, col = divmod(self.empty_tile_index, self.size)
        target_index = -1
        #Проверка хода
        if direction == 'u' and row > 0:
            target_index = self.empty_tile_index - self.size
        elif direction == 'd' and row < self.size - 1:
            target_index = self.empty_tile_index + self.size
        elif direction == 'l' and col > 0:
            target_index = self.empty_tile_index - 1
        elif direction == 'r' and col < self.size - 1:
            target_index = self.empty_tile_index + 1

        if target_index != -1:
            self.tiles[self.empty_tile_index], self.tiles[target_index] = self.tiles[target_index], self.tiles[self.empty_tile_index]
            self.empty_tile_index = target_index
    #Проверяет, решили ли мы игру.
    def is_solved(self):
        return self.tiles == list(range(1, self.size * self.size)) + [0]
    #Выводит текущее состояние игрового поля в консоль.
    def print_board(self):
        #os.system('cls' if os.name == 'nt' else 'clear')  # Очистка консоли
        #print("\033[H\033[J", end="")
        #subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        #clear = lambda: os.system('cls')
        #clear()
        print("\033[H\033[J")
        for i in range(self.size):
            row = self.tiles[i * self.size : (i + 1) * self.size]
            formatted_row = [str(tile).center(4) for tile in row]
            print(''.join(formatted_row))
#Функция для запуска и управления игрой "Пятнашки".
def play_game():
    size = 4  # Можно изменить размер поля
    game = Fifteen(size)
    while True:
        game.print_board()
        if game.is_solved():
            print("Поздравляем! Вы решили головоломку!")
            break
        move = input("Введите направление (u(up), d(down), l(left), r(right)) или 'q' для выхода: ").lower()
        if move == 'q':
            print("Выход из игры.")
            break
        elif move in ('u', 'd', 'l', 'r'):
            game.move(move)
        else:
            print("Неверное направление. Попробуйте еще раз.")

if __name__ == "__main__":
    play_game()