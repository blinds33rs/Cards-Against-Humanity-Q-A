import random

questions = open('CAH - Questions.txt')
answers = open('CAH - Answers.txt')


cardQuestionText = questions.readlines()
cardAnswerText = answers.readlines()


qcard = random.choice(cardQuestionText)
acard = random.choice(cardAnswerText)




print("The Question is: " + qcard + "\n")


print("The Answer is: " + acard+ "\n")
print("That's one funny robit, am I right?!")

#print(funny)




