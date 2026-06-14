# Student Profile System

name = input("Enter full name: ")

age_input = input("Enter age: ")
age = int(age_input)

gpa_input = input("Enter GPA: ")
gpa = float(gpa_input)

courses_input = input("Enter courses (comma-separated): ")
courses = courses_input.split(",")

student_profile = {
    "name": name,
    "age": age,
    "gpa": gpa,
    "courses": courses,
    "num_courses": len(courses)
}

deans_list = gpa >= 3.5
is_minor = age < 18

print("\n===== STUDENT PROFILE =====")
print(f"Name:        {student_profile['name']}")
print(f"Age:         {student_profile['age']} ({'Minor' if is_minor else 'Adult'})")
print(f"GPA:         {student_profile['gpa']}")
print(f"Courses:     {student_profile['courses']}")
print(f"# Courses:   {student_profile['num_courses']}")
print(f"Dean's List: {'Yes' if deans_list else 'No'}")
print("===========================")

print("\n===== TYPE CONVERSION =====")
print(f"Original age input type: {type(age_input)}")
print(f"Converted age type: {type(age)}")

print(f"Original GPA input type: {type(gpa_input)}") 
print(f"Converted GPA type: {type(gpa)}")

print(f"Original courses input type: {type(courses_input)}")
print(f"Converted courses type: {type(courses)}")
