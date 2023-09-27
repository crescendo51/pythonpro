import random as r

emoNum = r.randrange(0, 4)

if emoNum == 0:
  print('--------------')
  print('|            |')
  print('|  0      0  |')
  print('|     <      |')
  print('|            |')
  print('|  \      /  |')
  print('|   \    /   |')
  print('|    ----    |')
  print('--------------')

elif emoNum == 1:
  print('--------------')
  print('|            |')
  print('|  0      0  |')
  print('|     <      |')
  print('|            |')
  print('|            |')
  print('|   ------   |')
  print('|            |')
  print('--------------')

elif emoNum == 2:
  print('--------------')
  print('|            |')
  print('|  0      0  |')
  print('|     <      |')
  print('|            |')
  print('|    ----    |')
  print('|   /    \   |')
  print('|  /      \  |')
  print('--------------')

else :
  print("Illegal mood value!")
