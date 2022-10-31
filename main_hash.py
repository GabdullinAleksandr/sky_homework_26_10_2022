def get_hash(key):
    hash_val = ''
    for i in key:
        hash_val += str(ord(i))
    return hash_val, key


res = {}
while True:
    us_input = input('Введите ключ - ')
    print('Вывести таблицу - "print"')
    if us_input == 'print':
        print(res)
        continue
    s = get_hash(us_input)
    res[s[0]] = s[1]
