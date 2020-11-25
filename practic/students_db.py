groupmates = [
{
"name": "Александр",
"surname": "Иванов",
"exams": ["Информатика", "ЭЭиС", "Web"],
"marks": [4, 3, 5]
},
{
"name": "Иван",
"surname": "Петров",
"exams": ["История", "АиГ", "КТП"],
"marks": [4, 4, 4]
},
{
"name": "Кирилл",
"surname": "Смирнов",
"exams": ["Философия", "ИС", "КТП"],
"marks": [5, 5, 5]
},
{
"name": "Виктор Сергеевич",
"surname": "Сорокин",
"exams": ["Философия", "ИС", "КТП"],
"marks": [3, 2, 4]
},
{
"name": "Елена",
"surname": "Иванова",
"exams": ["3d", "ИС", "Web"],
"marks": [5, 4, 3]
},
{
"name": "Кирилл",
"surname": "Сорокин",
"exams": ["Философия", "ИС", "КТП"],
"marks": [5, 5, 5]
},
]

def count_mark(students,mark):
    print ("surname".ljust(15), "marks".ljust(20))
    for student in students:
        marks_list = student["marks"]
    result = (sum(marks_list)/len(marks_list))
    if result >= need:
        print(student["surname"].ljust(15), str(student["marks"]).ljust(20))

need = int(input('Input :'))

count_mark(groupmates,need)
