# Find the hieghest score in the class
#

student_scores = [78, 65, 89, 86, 55, 91, 64, 89,100]

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# Student Score Avarage

students = [
    {"name": "John", "score": 78},
    {"name": "Jack", "score": 65},
    {"name": "Jill", "score": 89},
    {"name": "James", "score": 86},
    {"name": "Jane", "score": 55},
    {"name": "Jenny", "score": 91},
    {"name": "Jade", "score": 64},
    {"name": "Jude", "score": 89},
    {"name": "Jasper", "score": 100}
]

# find the highest score
highest_score = 0
average_score = 0
student_name = ""
student_count = 0
for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        student_name = student["name"]
        student_count += 1
        average_score += student["score"]


print(f"The highest score in the class is: {highest_score} by {student_name}")
print(f"The average score in the class is: {round(average_score / student_count)}")
