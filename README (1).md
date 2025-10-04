# Test 1
student_name = "Ashton"
current_gpa = 3.0
study_hours = 10
social_points = 30
stress_level = 25
# social_points was evaluated from 0-30
# stress_level was evaluated from 0-25
print(f"Welcome: {student_name}")
print("Here are your stats: ")
print(current_gpa)
print(study_hours)
print(social_points)
print(stress_level)

# Test 2
print("Select the course load you would like to have:")
print("1) Light (not too much work and a ton of freetime) (12 credits)")
print("2) Standard (not a lot of work but a lot less freetime) (15 credits)")
print("3) Heavy (most work, least amount of freetime, beyond grief) (18 credits)")

choice = input("Your choice: ")

if choice == "1":
    if current_gpa >= 0:
        print("You have selected the 'LIGHT' course")
    else:
        print("You cannot take this course.")
elif choice == "2":
    if current_gpa >= 2.0:
        print("You have selected the 'STANDARD' course")
    else:
        print("You cannot take this course.")
elif choice == "3":
    if current_gpa >= 3.0:
        print("You have selected the 'HARD' course")
    else:
        print("You cannot take this course.")
elif choice is None:
    print("Invalid")
else:
    print("Invalid")
    # These if statements allows for the user to choose between 'LIGHT', 'STANDARD', and 'HARD' courses

# Test 3
study = ["Programming", "Math", "English", "History"]
print("Choose a class to study: ")
print(study)
choice = input("Choice selected: ")

if choice in study:
    if choice == "Programming":
        current_gpa += 0.2
        social_points -= 5
        print("You chose a pretty difficult subject, less free time more studying")
    elif choice == "Math":
        current_gpa += .3
        social_points -= 2
        print("Math huh?")
    elif choice == "English" and current_gpa >= 3.0:
        social_points += 10
        print("You have achieved balence, +10000 social credit")
    elif choice == "History" or (choice == "English" and current_gpa < 3.0):
        current_gpa += 0.1
        social_points += 3
        print("Good good, amazing actually, keep it up.")
    elif choice not in study:
        print("Invalid")
if study is not "Pyshics":
    print("Bomgos")
    # These if statements allows for the user to choose between which class they want to study, and depending on their choices, their GPA goes up regardless

  # Test 4
  print("Final Results: ")
print(f"GPA: {round(current_gpa, 2)}")
print(f"Study Hours: {study_hours}")
print(f"Stress {stress_level}")
print(f"Social Points {social_points}")

if current_gpa >= 3.0:
    print("Ending 1: Good grades")
elif current_gpa < 3.0:
    print("Ending 2: Bad grades. DO BETTER.")
elif current_gpa == 0:
    print("Ending 3: How is this possible?")
  #These if statements allow the game to end, which concludes the program and allows the user to get 1 of 3 unique endings.
  
