import os

student_list = [
    { "StudentName": "Sachin Tendulkar", "Hindi": 75, "Sanskrit": 65, "English": 58, "Social Science": 78, "Maths": 67, "Science": 72},
    { "StudentName": "Virat Kohli", "Hindi": 82, "Sanskrit": 90, "English": 85, "Social Science": 88, "Maths": 95, "Science": 80},
    { "StudentName": "Mithali Raj", "Hindi": 65, "Sanskrit": 70, "English": 75, "Social Science": 80, "Maths": 78, "Science": 85},
    { "StudentName": "P. V. Sindhu", "Hindi": 88, "Sanskrit": 92, "English": 90, "Social Science": 85, "Maths": 87, "Science": 93},
    { "StudentName": "Mary Kom", "Hindi": 74, "Sanskrit": 68, "English": 73, "Social Science": 77, "Maths": 75, "Science": 79},
    { "StudentName": "Sunil Chhetri", "Hindi": 90, "Sanskrit": 85, "English": 88, "Social Science": 84, "Maths": 82, "Science": 86},
    { "StudentName": "Saina Nehwal", "Hindi": 78, "Sanskrit": 80, "English": 85, "Social Science": 90, "Maths": 87, "Science": 84},
    { "StudentName": "Rohit Sharma", "Hindi": 20, "Sanskrit": 25, "English": 79, "Social Science": 45, "Maths": 92, "Science": 90},
    { "StudentName": "Neeraj Chopra", "Hindi": 76, "Sanskrit": 84, "English": 77, "Social Science": 82, "Maths": 80, "Science": 88},
    { "StudentName": "Hima Das", "Hindi": 81, "Sanskrit": 75, "English": 80, "Social Science": 78, "Maths": 82, "Science": 85},
    { "StudentName": "Vinesh Phogat", "Hindi": 77, "Sanskrit": 79, "English": 75, "Social Science": 72, "Maths": 85, "Science": 87},
    { "StudentName": "Anju Bobby George", "Hindi": 84, "Sanskrit": 86, "English": 88, "Social Science": 89, "Maths": 90, "Science": 92},
    { "StudentName": "Dutee Chand", "Hindi": 80, "Sanskrit": 82, "English": 83, "Social Science": 85, "Maths": 84, "Science": 86},
    { "StudentName": "Bajrang Punia", "Hindi": 82, "Sanskrit": 88, "English": 80, "Social Science": 86, "Maths": 89, "Science": 91},
    { "StudentName": "Geeta Phogat", "Hindi": 79, "Sanskrit": 75, "English": 78, "Social Science": 74, "Maths": 76, "Science": 82},
    { "StudentName": "Bhuvneshwar Kumar", "Hindi": 83, "Sanskrit": 85, "English": 82, "Social Science": 87, "Maths": 90, "Science": 89},
    { "StudentName": "Harmanpreet Kaur", "Hindi": 87, "Sanskrit": 90, "English": 93, "Social Science": 85, "Maths": 92, "Science": 90},
    { "StudentName": "Manpreet Singh", "Hindi": 70, "Sanskrit": 72, "English": 75, "Social Science": 73, "Maths": 77, "Science": 75},
    { "StudentName": "Smriti Mandhana", "Hindi": 88, "Sanskrit": 91, "English": 90, "Social Science": 87, "Maths": 89, "Science": 94},
    { "StudentName": "Kapil Dev", "Hindi": 75, "Sanskrit": 78, "English": 74, "Social Science": 79, "Maths": 83, "Science": 80}
]

os.system("cls")

for student in student_list:
    
    full_name = student["StudentName"]
    english = student["English"]
    sanskrit = student["Sanskrit"]
    hindi = student["Hindi"]
    maths = student["Maths"]
    social_studies = student["Social Science"]
    science = student["Science"]

    total = english + sanskrit + hindi + maths + social_studies + science 
    percentage = total / 6
    grade = None

    if english < 35 or sanskrit < 35 or hindi < 35 or maths < 35 or social_studies < 35 or science < 35:
        grade = "Fail"
    elif percentage >= 90:
        grade = "Merit"
    elif percentage >= 80:
        grade = "Dist"
    elif percentage >= 60:
        grade = "First Class"
    elif percentage >= 45:
        grade = "Second Class"
    elif percentage >= 35:
        grade = "Third Class"

    print("#" * 80)
    print("Markshit")
    print("#" * 80)
    print("Name of the Student:", full_name)
    print("-" * 80)
    print("English", english, sep=": ")
    print("Sanskrit", sanskrit, sep=": ")
    print("Hindi", hindi, sep=": ")
    print("Maths", maths, sep=": ")
    print("Social Studies", social_studies, sep=": ")
    print("Science", science, sep=": ")
    print("-" * 80)
    print("Total", total, sep=": ")
    print("Percent", percentage, sep=": ")
    print("Grade", grade, sep=": ")
    print()
