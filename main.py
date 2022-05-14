print ("Welcome to my first game in Python!!!")
name = input("What is your name? ")
age = int(input ("What is your age? "))
print("Hello",name,
      "Welcome to my game!",
      "Your are", age, "years old")


if age >= 12:
  print("You are old enough")

  want_to_play = input("Do you want to play?(yes or no) ")
  if want_to_play == "yes":
    print("Lets get started!")

  else: 
    print ("Goodbye!")
    
elif age <= 0 >= 0:
  print("Your not alive")
else:
  print ("You are not old enough")