from itertools import groupby

#HW_Task_3
def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))

#HW_Task_4
def thesaurus_adv(*args):
    s_n_sort = {}
    for s_n in args:
        s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
    return s_n_sort


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
                    "Борис Аркадьев", "Антон Серов", "Павел Анисимов"))