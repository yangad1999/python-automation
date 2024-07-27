user_name = input("Enter the user name: ")
user_qualification = input('Enter the user qualification [High School, Intermediate, Graduation and Post Graduation]')
user_age = float(input('Enter the user age: '))
user_experience = float(input('Enter your experience in years: '))

if user_qualification.lower() == "graduation" or user_qualification.lower() == "post graduation":
    print("You are eligible as per the qualififcation")
else :
    print("You are disqualified as per qualification")
    quit()

if user_age >= 18:
    print("You are eligible as per the age")
else:
    print("You are not eligible as per the age")
    quit()

if user_experience >= 5:
    print("You are eligible as per the experience")
else:
    print("You are not eligible as per the experience")
    quit()


print(user_name , "You are Qualified for the post ")



