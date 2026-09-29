user_age = int(input("Enter Your Age :"))

if user_age < 13:
	print("You Are  child")
elif (user_age <= 13 or user_age < 18):
	print("You Are Teenager")
elif (user_age <= 18 or user_age < 60):
	print("You Are An Adult")
elif (user_age >= 60):
	print("You are senior citizen")
else:
	print("Program finished")