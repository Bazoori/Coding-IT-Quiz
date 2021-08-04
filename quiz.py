score = 0

start = input("Would you like to start game?")
if start == "yes"or"Yes":
    question_1: print("When was Google Founded?")
    answer = input ("1986 / 2002 / 1998")
    if answer == "1998":
     print("Correct!")
     score = score+1
    else:
        print("Incorrect, The answer is 1998")


print("Your score is: ",score)
print("Next Question!")
question_2 = print("How many programming languages are there?")
answer_2 = input("350 / 700 / 500")
if answer_2 == "700":
        print("Correct!")
        score = score+1
else:
    print("Incorrect, The answer is 700")
print("Your score is: ",score)

print("Final Question!")
question_3 = print("Who was the first programmer?")
answer_3 = input("Ada Lovelace / Jeff Bezos / Niklaus Wirth").lower()
if answer_3 == "Ada Lovelace"or"ada lovelace":
    print("Correct!")
    score = score+1
else:
    print("Incorrect, The answer is A")
print("Your score is: ",score)

end = input("End Quiz?")
if end != "yes":
    print("Bye")
