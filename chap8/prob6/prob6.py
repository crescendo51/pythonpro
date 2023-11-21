import random

ran_num = random.randrange(0, 4)

print("\tWelcome to Trivia Challenge")
print('')
text_file = open("trivia.txt", "r")

for i in range(ran_num * 9) :
    text_file.readline()

title = text_file.readline()
category = text_file.readline()
question = text_file.readline()
answer1 = text_file.readline()
answer2 = text_file.readline()
answer3 = text_file.readline()
answer4 = text_file.readline()
correct_answer = int(text_file.readline())
explanation = text_file.readline()

print(title)
print(category)
print(question)
print("\t1 - ", answer1)
print("\t2 - ", answer2)
print("\t3 - ", answer3)
print("\t4 - ", answer4)
input_num = int(input("What's your answer?: "))

if input_num == correct_answer :
    print("You got the answer!")
    print(explanation)
else :
    print("You're wrong!")
    print("The answer was", correct_answer)
    print(explanation)
