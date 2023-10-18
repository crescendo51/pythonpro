inputNum = 1

geek = {"404" : "clueless.", "Uninstalled" : "being fired."}

while inputNum != 0 :
  print("\tGeek Translator")
  print('')
  print("\t0 - Quit")
  print("\t1 - Look Up a Geek Term")
  print("\t2 - Add a Geek Term")
  print("\t3 - Redefine a Geek Term")
  print("\t4 - Delete a Geek Term")
  print('')
  inputNum = int(input("Choice: "))
  print('')

  if inputNum == 1 :
   word =  input("What term do you want me to translate?: ")
   if word in geek :
       print(word + " means " + geek[word])
       print('')
   else :
       print("None")
       print('')

  if inputNum == 2 :
      addWord = input("What term do you want me to add?: ")
      meaning  = input("Please tell me what this word means: ")
      geek[addWord] = meaning

  if inputNum == 3 :
      redefWord = input("What term do you want to redefine?: ")
      redefine = input("Please tell me what this word means: ")
      geek[redefWord] = redefine

  if inputNum == 4 :
      delWord = input("What term do you want to remove?: ")
      del(geek[delWord])
      print('')
