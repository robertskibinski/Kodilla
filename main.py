exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []
best_student = []
# best_student = ("",0)
for person in exam_points.items():
    if person[1] <= 45:
        failed_students.append(person[0])
    elif person[1]>=91:
        top_students.append(person[0])
        best_student.append(person)
best_student=tuple(best_student)
print(failed_students)
print(top_students)
print(best_student)