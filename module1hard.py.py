students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students2 = list(students)
students2.sort()
u =list(map(sum,(grades)))
r = list(map(len,(grades)))
def create_list(a, b):
    return a/b
x = list(map(create_list, u ,r ))
def create_dict (a, b):
    return a, b
my_new_dict = map(create_dict, students2,x)
print(dict(my_new_dict))
