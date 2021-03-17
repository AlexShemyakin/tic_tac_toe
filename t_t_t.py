k = 0
table_main = '0 | 1 | 2\n--|---|--\n3 | 4 | 5\n--|---|--\n6 | 7 | 8'
result_1 = []
rslt_2 = []


def Game(table):
    global result_1
    global rslt_2
    if (((0 in result_1) and (1 in result_1) and (2 in result_1)) or (3 in result_1 and 4 in result_1 and 5 in result_1)
            or (6 in result_1 and 7 in result_1 and 8 in result_1) or
            (0 in result_1 and 3 in result_1 and 6 in result_1)
            or (1 in result_1 and 4 in result_1 and 7 in result_1) or
            (2 in result_1 and 5 in result_1 and 8 in result_1)
            or (0 in result_1 and 4 in result_1 and 8 in result_1) or
            (2 in result_1 and 4 in result_1 and 6 in result_1)):
        print("Второй игрок выйграл! Поздравляю!")
        return
    elif ((0 in rslt_2 and 1 in rslt_2 and 2 in rslt_2) or (3 in rslt_2 and 4 in rslt_2 and 5 in rslt_2)
          or (6 in rslt_2 and 7 in rslt_2 and 8 in rslt_2) or (0 in rslt_2 and 3 in rslt_2 and 6 in rslt_2)
          or (1 in rslt_2 and 4 in rslt_2 and 7 in rslt_2) or (2 in rslt_2 and 5 in rslt_2 and 8 in rslt_2)
          or (0 in rslt_2 and 4 in rslt_2 and 8 in rslt_2) or (2 in rslt_2 and 4 in rslt_2 and 6 in rslt_2)):
        print("Первый игрок оказался сильнее!")
        return

    global k
    k += 1
    if k % 2 == 0:
        hod = input('Ход второго игрока: ')
        table = table.replace(hod, 'O')
        result_1.append(int(hod))
        print(table)
    else:
        hod = input('Ход первого игрока: ')
        table = table.replace(hod, 'X')
        rslt_2.append(int(hod))
        print(table)
    return Game(table)


print('0 | 1 | 2\n--|---|--\n3 | 4 | 5\n--|---|--\n6 | 7 | 8')
Game(table_main)
