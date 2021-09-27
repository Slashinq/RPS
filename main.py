import random
a = str(input(""))
b = random.randint(0,2)
# 0 is Rock
# 1 is Paper
# 2 is Scissor
if a == "Rock" and b == 0:
    print("You picked: Rock")
    print("Computer picked: Rock")
    print("It's a draw!")
elif a == "Rock" and b == 1:
    print("You picked: Rock")
    print("Computer picked: Paper")
    print("You lose :(")
elif a == "Rock" and b == 2:
    print("You picked: Rock")
    print("Computer picked: Scissor")
    print("You win!")
elif a == "Paper" and b == 0:
    print("You picked: Paper")
    print("Computer picked: Rock")
    print("You win!")
elif a == "Paper" and b == 1:
    print("You picked: Paper")
    print("Computer picked: Paper")
    print("It's a draw!")
elif a == "Paper" and b == 2:
    print("You picked: Paper")
    print("Computer picked: Scissor")
    print("You lose :(")
elif a == "Scissor" and b == 0:
    print("You picked: Scissor")
    print("Computer picked: Rock")
    print("You lose :(")
elif a == "Scissor" and b == 1:
    print("You picked: Scissor")
    print("Computer picked: Paper")
    print("You win!")
elif a == "Scissor" and b == 2:
    print("You picked: Scissor")
    print("Computer picked: Scissor")
    print("It's a draw!")
else:
    print("Input was invalid")
