
def create_mass(lenght):
    return [None for _ in range(lenght)]


def reading_mass(item, lst, logic_size):
    if item < logic_size:
        return lst[item]
    else:
        return False


def mass_entry(item_entry, lst, logic_size):
    lst[logic_size] = item_entry
    logic_size += 1
    return logic_size


def removal_mass(us_input, lst, logic_size):
    lst[us_input] = None
    for i in range(us_input, logic_size):
        if i == logic_size - 1:
            logic_size -= 1
            return logic_size
        if lst[i] is None:
            lst[i], lst[i + 1] = lst[i + 1], None


def insert_mass(us_input_id, item_insert, lst, logic_size):
    if logic_size == us_input_id:
        return mass_entry(item_insert, lst, logic_size)
    elif us_input_id > logic_size:
        print('Неверный ввод')
        quit()
    else:
        for i in range(logic_size, us_input_id - 1, - 1):
            if i == us_input_id:
                lst[i] = item_insert
                logic_size += 1
                return logic_size
            s = lst[i-1]
            lst[i] = s
