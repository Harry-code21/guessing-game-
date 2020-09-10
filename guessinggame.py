random_no = 73
guess=1
num=int (input("enter a number"))
game_over=False

while not game_over:
    if num==random_no:
         print(f"you won !!!,you guessed no in {guess} times")
         game_over=True
    else:
        if num>random_no:
             print("too high")
             guess=guess+1
             num=int(input("enter again:"))
        else:
             
             print("too low")
             guess=guess+1
             num=int(input("enter again:"))
            
 
