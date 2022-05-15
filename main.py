print ("Welcome to my first game in Python!!!")
name = input("What is your name? ")
age = int(input ("What is your age? "))
print("Hello",name,
      "Welcome to my game!",
      "Your are", age, "years old")

#Health
health = 10

#Shield
sh = 0

#Age System
if age >= 12:
  print("You are old enough")

  '''Do you want to play'''
  want_to_play = input("Do you want to play?(yes/no) ").lower()
  if want_to_play == "yes":
    print("Lets get started!")

    print("You are starting with", health, "health")

    #Story
    print ("You meet yourself in front of a mossy rock with the path you been following for hours diverges. The right path leads to a forest while the left leads to some hilly area, but its to far to see anything else.")
    l_o_r = input("Do you wanna go left or right (left/right)? ").lower()


    
    #Left path
    if l_o_r == "left":
      print ("You followed the path left for 10 minutes. Until you hear a strange noise")
      ll = input("Do you go back and head right?(yes/no) ").lower()
      
      if ll == "yes":
        print ("You decided it was to dangerous. So, you went the other way.")
        l_o_r = "right"
        
        
      elif ll == "no":
          print("You head towards the noise. Those strange noises was coming from a lively festival in a small village.") 
          print("As you came near the village. You can see the colourful lights and the bright clothing. Filled with many colours and patterns. From men to women wearing long drapes of cloth. Some had colourful earings.")
          print("You went into the village wandering the place. Until you found yourself with more options.")
      vil = input("Where would you like to go?(tavern/outside/chief)" ).lower()

elif vil == "tavern":
        print ("You decided to go into the tavern. You can smell the booze in the air. You can even hear a drunk guy in the corner. Another person is playing a instrument in a shape of a uke. While there is someone who stands out at the bar.")
tav = input("Who would you like to talk to?(drunkard/uke/bar) ").lower()
      
if tav == "drunkard":
  print ("You went to the drunk guy in the corner. You ask if he was alright. He babbled at you. Saying nothing you can understand. It was pure gibberish in your ears. He could not make a complete sentence.")
vil == "tavern"

if tav == "uke":
  print("N/A")


if tav == "bar":
  print("N/A")

      

      
if vil == "outside":
  print("N/A")


if vil == "chief":
  print("N/A")

        
      

    #Right path
  if l_o_r == "right":
        print("You walk into the forest. It suddenly got dark.What do you do. You can barely see whats ahead of you.")
  rr = input("Do you go back?(yes/no) ").lower()

  if rr == "yes":
    print("N/A")

  if rr == "no":
    health -= 7
    print("As you went forward. You were attack. Your health is know at", health, "health. You kept on going until you were at a clearing. There was no trees and the sun shine right above you. Though know you find yourself in front of two choices. Both path looks dark and there is no way in telling what each path might have at the end.")
    rr2 = input("Do you head right or left?(right/left) ").lower()

    if rr2 == "test":
        health -= 3
        print(health,"health")

    if health <= 0:
        print("You died! ;-;")

      

  else: 
    print ("Goodbye!")

    #Age system
elif age <= 0 >= 0:
  print("Your not alive")
else:
  print ("You are not old enough")