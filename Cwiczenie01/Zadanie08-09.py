student_list = (
    (151206, "Oskar Majewski"),
    (152312, "Kamil Kamilow"),
    (124353, "Jan Man"),
)
print(student_list)

diccct = {}
for i in student_list:
    diccct[i[0]] = {
        "name": i[1],
        "age": None,
        "email": None,
        "year": None,
        "adres": None,
    }
print(diccct)
