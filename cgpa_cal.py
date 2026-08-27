name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))

total_grade_points = 0

for i in range(num_subjects):
    grade_point = float(input(f"Enter grade point for subject {i + 1}: "))
    total_grade_points += grade_point

cgpa = total_grade_points / num_subjects

print("\n--- Student Result ---")
print("Student Name:", name)
print("Final CGPA:", round(cgpa, 2))