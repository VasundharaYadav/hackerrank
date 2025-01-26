n = int(input())

students = []

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted({student[1] for student in students})  
second_lowest_grade= grades[1]

names_with_second_lowest = [student[0] for student in students if student[1] == second_lowest_grade]

names_with_second_lowest.sort()

for name in names_with_second_lowest:
    print(name)
