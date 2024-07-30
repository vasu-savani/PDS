Students_Data = {
    1: {"id_no": 1, "name": "Vasu", "marks": 85},
    2: {"id_no": 2, "name": "Kevin", "marks": 90},
    3: {"id_no": 3, "name": "Jay", "marks": 78},
    4: {"id_no": 4, "name": "Parth", "marks": 92},
    5: {"id_no": 5, "name": "Vedant", "marks": 88}
}

keys_list = list(Students_Data.keys())
values_list = list(Students_Data.values())

print("Keys list:", keys_list)
print("Values list:", values_list)

Students_Data[6] = {"id_no": 6, "name": "Vidja", "marks": 95}

print("Updated Students Data:", Students_Data)

id_no = 3
student_data = Students_Data.get(id_no)
if student_data:
    print("Student data for id_no", id_no, ":", student_data)
else:
    print("Student data for id_no", id_no, "not found")

def update_detail(k, new_data):
    for key, value in Students_Data.items():
        if key == k:
            Students_Data[key] = new_data
            return Students_Data
    print("Student data for id_no", k, "not found")
    return Students_Data

updated_data = {"id_no": 3, "name": "Jay updated", "marks": 95}
Students_Data = update_detail(3, updated_data)

print("Updated Students Data:", Students_Data)

keys_list = []
for key in Students_Data.keys():
    keys_list.append(key)

print("Keys list:", keys_list)

values_list = list(Students_Data.values())

print("Values list:", values_list)

total_students = len(Students_Data)
print("Total number of students:", total_students)

Students_Data.clear()
print("Cleared Students Data:", Students_Data)

exam_data_array = {
    'name': ['Vasu', 'Kevin', 'Jay', 'Parth', 'Vedant'],
    'core': [85, 90, 78, 92, 88],
    'attempts': [1, 2, 3, 4, 5],
    'qualify': [True, True, False, True, True]
}

print("Exam data array:", exam_data_array)

exam_data_list = [
    {'name': 'Vasu', 'core': 85, 'attempts': 1, 'qualify': True},
    {'name': 'Kevin', 'core': 90, 'attempts': 2, 'qualify': True},
    {'name': 'Jay', 'core': 78, 'attempts': 3, 'qualify': False},
    {'name': 'Parth', 'core': 92, 'attempts': 4, 'qualify': True},
    {'name': 'Vedant', 'core': 88, 'attempts': 5, 'qualify': True}
]

print("Exam data list:", exam_data_list)