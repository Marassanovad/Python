# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена,
#  начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 
# 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

lines = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]


def FIO(lines: list):
    result = {}
    for name in lines:
        if name[0] not in result:
            result[name[0]] = [name]
        else:
            result[name[0]].append(name)
    return result


def sort(ls):
    for key in sorted(ls):
        print(key, '=>', ls[key])


sort(FIO(lines))