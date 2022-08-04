# dictionary comprehension
# new_dict = {new_key: new_value for item in list}

# new_dict1 = {new_key: new_value for (key, value) in dict.items()}

# new_dict2 = {new_key: new_value for (key, value) in dict.items() if test}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed_students)


sentence = "What is the Airspeed velocity of an Unladen Sallow?"
new_sentence = {word: len(word) for word in sentence.split()}
print(new_sentence)

weather = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

new_weather = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather.items()}
print(new_weather)

# for temp in weather:
#     temp_f = (int(temp) * 9/5) + 3
#    print(temp_f)


"""How to iterate over a Pandas DataFrame"""
student_dic = {
    "student": ["Angela", "James", "Lily"],
    "Score": [56, 76, 98]
}

# lopping through dictionaries:
for (key, value) in student_dic.items():
    print(key, value)
    print(key)
    print(value)

# down code creates a table and for each of keys and values writes a number in front of them and then write them.
# like 0 Angela 56
import pandas

student_data_frame = pandas.DataFrame(student_dic)
print(student_data_frame)

# loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# loop through rows of a data frame:
for(index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.Score)
