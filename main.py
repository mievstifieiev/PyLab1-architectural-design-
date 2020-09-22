import Room
import Teacher, Human, Student

st_name = "1"
st_mass = []

while st_name:
    st_name = input("Students enter the classroom: ")
    if st_name:
        st_mass.append(Student.Student(st_name))

t_name = input("The teacher enter the classroom: ")
ro = Room.Room(st_mass, Teacher.Teacher(t_name))
a = "Да"
while a=="Да":
    ro.Start_lection()
    a = input("Продолжить?")


