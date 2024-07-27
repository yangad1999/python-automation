
########## Normal Print ##########

print("Welcome to Quinnox")

########## Marksheet App ##########

first_name = 'Angad'
last_name = "Yadav"

english = 65
sanskrit = 75
hindi = 85
maths = 75
social_studies = 90
science = 72

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
print("Name of the Student:", first_name, last_name)
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
