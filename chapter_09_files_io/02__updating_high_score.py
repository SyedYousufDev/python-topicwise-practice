import random

def game():
    print("You are playing Random number game")
    
    score=random.randint(1,100)
       
    with open("02_high_score.txt") as f:
      hiscore=f.read()
      if (hiscore!=""):
        hiscore= int(hiscore)
      else:
         hiscore=0  
    
    if(score>hiscore):
     with open("02_high_score.txt","w") as f:
      f.write(str(score))


    return score



print(f"Your Score is {game()}")