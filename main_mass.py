from utlis_mass import *


def main():
    us_input = int(input('Введите нужную длину массива - '))
    lst = create_mass(us_input)
    logic_size = 0
    while True:
        if lst[-1] is not None:
            print('массив заполнен')
            print(lst)
            quit()
        us_input = int(input("""Выберите действие:
            1 - Чтение 
            2 - Запись
            3 - Удаление
            4 - Вставка
            5 - Вывести массив    
        """))
        match us_input:
            case 1:
                us_input = int(input('Какой элемент нужен?(индекс) - '))
                res = reading_mass(us_input, lst, logic_size)
                if res:
                    print(res)
                else:
                    print('Неверный ввод')
            case 2:
                us_input = input('Что записать? - ')
                logic_size = mass_entry(us_input, lst, logic_size)
            case 3:
                us_input = int(input('Какой элемент удалить?(индекс) - '))
                if us_input >= logic_size:
                    print('Неверный ввод')
                    continue
                logic_size = removal_mass(us_input, lst, logic_size)
            case 4:
                us_input_id = int(input('На какую позицию вставить?(индекс) - '))
                us_input = input('Что записать? - ')
                logic_size = insert_mass(us_input_id, us_input, lst, logic_size)
            case 5:
                print(lst)
            case 6:
                print(logic_size)
            case _:
                print('Неверный ввод')


if __name__ == '__main__':
    main()
