Subjects = []
for i in range(1, 11):
    Subjects.append(f"Subject {i}")

Elective_Subjects = ["Elective 1", "Elective 2", "Elective 3", "Elective 4", "Elective 5"]
Subjects.extend(Elective_Subjects)

Subjects.append("Subject 1")
Subjects.append("Subject 1")
Subjects.append("Subject 1")

index = Subjects.index("Subject 1")
while "Subject 1" in Subjects:
    Subjects.remove("Subject 1")

def remove_range(i1, i2):
    del Subjects[i1:i2]
    return Subjects

Subjects = remove_range(3, 5)

Subjects.reverse()
Subjects.sort()

popped_element = Subjects.pop(4)

total_elements = len(Subjects)

Subjects.clear()

my_tuple = ("a", "b", "c", "d", "e")
my_list = list(my_tuple)
my_list[2] = "x"
my_list.remove("d")
my_tuple = tuple(my_list)

print("Initial Subjects list:", Subjects)
print("Elective Subjects list:", Elective_Subjects)
print("Extended Subjects list:", Subjects)
print("Subjects list with duplicates:", Subjects)
print("Index of first occurrence of duplicate value:", index)
print("Subjects list after removing duplicates:", Subjects)
print("Subjects list after removing range:", Subjects)
print("Reversed and sorted Subjects list:", Subjects)
print("Popped element:", popped_element)
print("Subjects list after popping:", Subjects)
print("Total elements in the list:", total_elements)
print("Cleared Subjects list:", Subjects)
print("Updated tuple:", my_tuple)