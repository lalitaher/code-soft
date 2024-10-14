# """
# WORKFLOW OF PROJECT
# 1-Input from user(rock,paper scissor)
# 2-Computer choice(Computer will choose randomely not conditionally)
# 3-Result Print

# Cases:
# A-Rock
# Rock-Rock=tie
# Rock-paper=Paper win
# Rock-scissor=Rock win

# B=Paper
# Paper-Paper=tie
# Paper-Rock=Paper win
# Paper-Scissor=Scissor win

# C=Scissor
# Scissor-Scissor=tie
# Scissor-Rock=Rock
# Scissor-paper=Scissor win





# """
import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your move=Rock,Paper,Scissor=")


comp_choice=random.choice(item_list)
print("user choice=",user_choice)
print("computer choice=",comp_choice)

if(user_choice==comp_choice):
    print("Both choice are same=match tie")
elif(user_choice=="Rock"):
    if(comp_choice=="Paper"):
      print(" Paper covers Rock=Paper win")
    else:
       print("Rock brake scissor=you win")
elif(user_choice=="Paper"):
   if(comp_choice=="Scissor"):
      print("scissor cuts paper=computer win")
   else:
      print("paper covers Rock=you win")
elif(user_choice=="Scissor"):
   if(comp_choice=="Rock"):
      print("Rock break scissor=computer win")
   else:
      print("scissor cuts paper=computer win") 
