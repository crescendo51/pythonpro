import random

count = 6
word = ['difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university']
select_word = random.choice(word)
char_list = []

print(select_word)
while True:
    input_char = input("Enter your guess: ")
    char_list += input_char
    

    print('')
    if input_char in select_word :
      print("Yes! " + input_char + " is in the word!")
    else :
        print("No!" + input_char + " is not in the word!")
        count -= 1

    if count == 6:
      print(" ______")
      print(" |    |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print("==========")
      print('')
      print('')
        
    elif count == 5: 
      print(" ______")
      print(" |    |")
      print(" |    O")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print("==========")
      print('')
      print('')

    elif count == 4:
      print(" ______")
      print(" |    |")
      print(" |    O")
      print(" |    +")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print("==========")
      print('')
      print('')

    elif count == 3:
      print(" ______")
      print(" |    |")
      print(" |    O")
      print(" |   -+")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print("==========")
      print('')
      print('')

    elif count == 2:
      print(" ______")
      print(" |    |")
      print(" |    O")
      print(" |   -+-")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print("==========")
      print('')
      print('')

    elif count == 1:
      print(" ______")
      print(" |    |")
      print(" |    O")
      print(" |   -+-")
      print(" |   /  ")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print("==========")
      print('')
      print('')

    print("You've used the following letters: ")
    print(char_list)

    for i in select_word :
        if i in char_list :
          print(i, end = '')
        else :
          print("-", end = '')
   
    print('')
    if set(select_word) == set(char_list) :
        print("YOU WIN")
        break
    if count == 0 :
      print(" ______")
      print(" |    |")
      print(" |    O")
      print(" |   -+-")
      print(" |   / \\")
      print(" |")
      print(" |")
      print(" |")
      print(" |")
      print("==========")
      print("YOU LOSE")
      break
