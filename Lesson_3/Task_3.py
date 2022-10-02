def regres(a,b):
    result = []
    while a != 0:
        result.append(a % b)
        a = a//b
    result.reverse()
    return result
num = 11
razraydnost = 2
print(*regres(num, razraydnost))



# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# action = str(input(*Choose action: Add(a), Sub(S)
# Mult(m) Div(d) ->"))
# print("The result is "end=*)
# If action == "a";
# print(num1+num2)
# elif action == 's":
# print(num1-num2)
# elif action == "m':
# print(num1*num2)
# else:
# print(num1/num2)