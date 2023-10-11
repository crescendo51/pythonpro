inputNum = 1
scores_list = []

while inputNum != 0 :
  print("\t High Scores Keeper")
  print('')
  print("\t0 - Quit")
  print("\t1 - List Scores")
  print("\t2 - Add a Score")
  print('')
  inputNum = int(input("Choice: "))
  print('')

  if inputNum == 1 :
    print("High Scores")
    print('')
    print("NAME\tScores")
    for entry in scores_list:
      new_name, new_score = entry
      print(new_name, "\t", new_score)
    print('')

  if inputNum == 2 :
    new_name = input("What is the player's name?: ")
    new_score = int(input("What score did the player get?: "))
    scores_list.append((new_name ,new_score))
    scores_list.sort(key = lambda x:x[1], reverse = True)
    print('')
