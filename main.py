print ("Welcome to my first game in Python!!!")
name = input("What is your name? ")
age = int(input ("What is your age? "))
print("Hello",name,
      "Welcome to my game!",
      "Your are", age, "years old")

'''Health'''
health = 10

'''Age System'''
if age >= 12:
  print("You are old enough")

  '''Do you want to play'''
  want_to_play = input("Do you want to play?(yes/no) ").lower()
  if want_to_play == "yes":
    print("Lets get started!")

    print("You are starting with", health, "health")

    '''Story'''
    print ("You meet yourself in front of a mossy rock with the path you been following for hours diverges. The right path leads to a forest while the left leads to some hilly area, but its to far to see anything else.")
    l_o_r = input("Do you wanna go left or right (left/right)? ")


    
    '''Left path'''
    if l_o_r == "left":
      print ("You followed the path left for 10 minutes. Until you hear a strange noise")
      ll = input("Do you go back and head right?(yes/no) ").lower()

      if ll == "yes":
        l_o_r = "no"
        print ("You decided it was to dangerous. So, you went the other way.")
      elif ll == "no":
          print("You head towards the noise. Those strange noises were coming from a lively festival in a small village.")
      

    '''Right path'''
    if l_o_r == "no":
      print("You walk into the forest. It suddenly got dark.What do you do. You can barely see whats ahead of you.")
      rr = input("Do you go back?(yes/no) ").lower()

    if rr == "yes":
      print("N/A")

    if rr == "no":
      print("N/A")

      

  else: 
    print ("Goodbye!")

    '''Age System'''
elif age <= 0 >= 0:
  print("Your not alive")
else:
  print ("You are not old enough")