# 1. Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции +,-,/,*
# приоритет операций стандартный. Добавьте скобки, приоритет операций меняется.


actions = {
    "^": lambda x, y: float(x) ** float(y),
    "*": lambda x, y: float(x) * float(y),
    "/": lambda x, y: float(x) / float(y),
    "+": lambda x, y: float(x) + float(y),
    "-": lambda x, y: float(x) - float(y)
}


def hooks(ls):
    if set(ls).isdisjoint('(' or ')'):
        return ls
    else:
        hoo1 = ls.index('(')
        hoo2 = ls.index(')')
        a = actions[ls[hoo1+2]](ls[hoo1+1], ls[hoo2-1])
        ls[hoo2] = a
        del ls[hoo1:hoo2]
        return (ls)


def dolist(string):
    ls = string.split()


def multiplication(ls):
    if '*' or '/' in ls:
        if '*' in ls:
            sym = ls.index('*')
        else:
            sym = len(ls)-1
        
        if '/' in ls:
            sym2 = ls.index('/')
        else:
            sym2 = len(ls)-1
        
        if sym <= sym2:
            res = actions[ls[sym]](ls[sym-1], ls[sym+1])
            ls[sym+1] = res
            del ls[sym-1:sym+1]
            return (ls)
        else:
            res = actions[ls[sym2]](ls[sym2-1], ls[sym2+1])
            ls[sym2+1] = res
            del ls[sym2-1:sym2+1]
            return (ls)
    else:
        print('Error')
        return ls


def addition(ls):
    if '+' or '-' in ls:
        if '+' in ls:
            sym = ls.index('+')
        else:
            sym = len(ls)
        if '-' in ls:
            sym2 = ls.index('-')
        else:
            sym2 = len(ls)
        if sym < sym2:
            res = actions[ls[sym]](ls[sym-1], ls[sym+1])
            ls[sym+1] = res
            del ls[sym-1:sym+1]
            return (ls)
        else:
            res = actions[ls[sym2]](ls[sym2-1], ls[sym2+1])
            ls[sym2+1] = res
            del ls[sym2-1:sym2+1]
            return (ls)
    else:
        print('Error')
        return ls


def arithmetic(ls):
    if '(' in ls:
        hooks(ls)

    while '*' or '/' in ls:
        multiplication(ls)
        print(ls)
        return ls


li = ['20', '', '5', '', '8', '', '2', '1']
# print(addition(li))
print(multiplication(li))

# arithmetic(li)
# hooks(li)

# while True:
#     if '*' or '/' in li:
#         multiplication(li)
#     else: break

# print(li)
