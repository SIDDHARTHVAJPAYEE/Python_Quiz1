print("Hello! Welcome to Quiz")
ans =input("Are you ready to play the Quiz:(y/n) ")
score=0  
totalques=10 
if ans.lower()=="yes" or ans.lower()=="y": # lower() functions changes all letters in small letters in string. 
  ans=input("1. What is the most famous programming language ?")
  if ans.lower()=="python":
    score+=1
    print("Correct")
  else:
    print("Incorrect")


  ans=input("2. What is 13*5 ?")
  if ans.lower()=="65":
    score+=1
    print("Correct")
  else:
    print("Incorrect")

  ans=input("3. What is the capital of India ?")
  if ans.lower()=="delhi" or ans.lower()=="new delhi" or ans.lower()=="newdelhi": # there could be different ways of writing the right answer we need to check all conditions. 
    score+=1
    print("Correct")
  else:
    print("Incorrect")

  # Add 7 more questions like this.   

print("Thank you for playing, your total right answers were: ", score)

mark=(score/totalques)*100 # We will calculate the percentage of score. 

print("Marks: ", mark,"% ")

if mark>80:
  print("Very Good. You were excellent.")
elif mark>60 and mark<=80:
  print("You did well. Try to make it better.")
else:
  print("Try again. ")

print("Good Luck. ")
