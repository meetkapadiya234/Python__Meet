student = {
    "name": "meet",
    "email":"meet@gmiala.com",
    "sub": ["python", "java", "c++"],
}
# print(student)
# print(student["name1"])
# print(student.get("name1",))

# print(student.keys())
# print(student.values())
# print(student.items())

print(student["sub"][1])
student["name1"] = "Met"
student["name"] = "Met"
print(student)

for i in student:
    print(i, ":", student[i])

for i in student.items():
    print(i)



