# 5. ** Даны два файла, в каждом из которых находится запись многочленов. 
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0 
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!


with open('poly.txt') as file:
	lst = file.read()
	lines = lst.count('\n') + 1


with open('poly2.txt') as file1:
	lst2 = file1.read()
	lines2 = lst2.count('\n') + 1


if  lines != lines2:
    print('The contents of the files do not match!')

else:
    first_filename = "poly.txt"
    second_filename = "poly2.txt"


    with open(first_filename, 'r') as file:
        first_file_content = file.read()

    with open(second_filename, 'r') as file:
        second_file_content = file.read() 

    print(first_file_content and second_file_content)



	
	
