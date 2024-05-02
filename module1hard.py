grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
students = list(sorted(students))

grades = [i.split() for i in grades]

grades_1 = list(map(int, grades[0]))
grades_2 = list(map(int, grades[1]))
grades_3 = list(map(int, grades[2]))
grades_4 = list(map(int, grades[3]))
grades_5 = list(map(int, grades[4]))

my_dict = {students[0]: sum(grades_1) / len(grades_1), students[1]: sum(grades_2) / len(grades_2), students[2]: sum(grades_3) / len(grades_3), students[3]: sum(grades_4) / len(grades_4), students[4]: sum(grades_5) / len(grades_5)}
print(my_dict)