student_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 88,
    "David": 90
}
unique={}
for i,j in student_grades.items():
    if j not in unique.values():
        unique[i]=j #add
print(unique)