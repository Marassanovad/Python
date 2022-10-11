# 3. * Создайте программу для игры в "Крестики-нолики". 
# Поле 3x3. Игрок - игрок, без бота.

win_position = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]]
   
map =  [1, 2, 3,
        4, 5, 6,
        7, 8, 9]


def create_map():
    # os.system('cls' if os.name == 'nt' else 'clear')       
    print(' ', map[0], end=" | ")
    print(map[1], end=" | ")
    print(map[2])
    print('------------')

    print(" ", map[3], end=" | ")
    print(map[4], end=" | ")
    print(map[5])
    print('------------')

    print(" ", map[6], end=" | ")
    print(map[7], end=" | ")
    print(map[8])
   


create_map()
