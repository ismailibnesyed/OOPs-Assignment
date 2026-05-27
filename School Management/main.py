from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABC", "Dhaka")

# classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

# add classroom
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Student
rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hahim = Student("Hahim", ten)

# adding student in school admission
school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hahim)

# Adding Teacher
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kbul = Teacher("Kbul Khan")

# adding subject with teacher 
bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kbul)
biology = Subject("Biology", kbul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(chemistry)
ten.add_subject(biology)

eight.take_semister_final_exam()
nine.take_semister_final_exam()
ten.take_semister_final_exam()

print(school)