import random as r

count = 0

heroHp = r.randrange(50, 101)
monHp = r.randrange(50, 101)
# random HP

print("hero HP: ", heroHp, ", monster HP: ", monHp, sep ="")

while heroHp >= 0 and  monHp >= 0 :
  heroAtk = r.randint(-10, 21)
  monAtk = r.randint(-10, 21)
# random attack damage

  if heroAtk > 0 and monAtk > 0 :
    heroHp = heroHp - monAtk
    monHp = monHp - heroAtk
    print("hero(HP:", heroHp, ", attack:", heroAtk, ") success <-> monster(HP:", monHp,     ", attack:", monAtk, ") success")
    count = count + 1
# heroAtk success, monAtk success

  elif heroAtk > 0 and monAtk < 0 :
    monHp = monHp - heroAtk
    print("hero(HP:", heroHp, ", attack:", heroAtk, ") success <-> monster(HP:", monHp,     ", attack:", monAtk, ") fail")
    count = count + 1
# heroAtk success, monAtk fail

  elif heroAtk < 0 and monAtk > 0 :
    heroHp = heroHp - monAtk
    print("hero(HP:", heroHp, ", attack:", heroAtk, ") fail <-> monster(HP:", monHp,        ", attack:", monAtk, ") success")
    count = count + 1
# heroAtk fail, monAtk success

  elif heroAtk < 0 and monAtk < 0 : 
    print("hero(HP:", heroHp, ", attack:", heroAtk, ") fail <-> monster(HP:", monHp,        ", attack:", monAtk, ") fail")
    count = count + 1

# heroAtk fail, monAtk fail

print("---------------------------------------------------------------------------------------")

print("Total phase:", count)
if heroHp <= 0 :
  print("Monster Win!!!!")
elif monHp <= 0 :
  print("Hero Win!!!!")



