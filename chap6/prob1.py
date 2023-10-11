items = ["sword", "armor", "shield", "healing potion"]

print("Your items:")

for i in range(0 ,len(items)) :
  print(items[i])

print('')
print("Press the enter key to continue.")
print("You have " + str(len(items)) + " items in your possession.")
print('')
print("Press the enter key to continue.")

if "healing potion" in items :
  print("You will live to fight another day.")

print('')
inputNum = int(input("Enter the index number for an item in inventory: "))
print("At index " + str(inputNum) + " is " + items[inputNum])

print('')
startSliceNum = int(input("Enter the index number to begin a slice : "))
endSliceNum = int(input("Enter the index number to end the slice : "))
print("inventory[ " + str(startSliceNum) + " : " + str(endSliceNum) + " ]\t\t", end = '')
print(items[startSliceNum : endSliceNum])

print('')
print("Press the enter key to continue.")

chest = ["gold", "gems"]
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
items += chest
print(items)
print('')
print("Press the enter key to continue.")
print("You trade your sword for a crossbow.")
items[0] = "crossbow"
print("Your inventory is now:")
print(items)
print('')

print("Press the enter key to continue.")
print("You use your gold and gems to buy an orb or future telling.")
items[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(items)
print('')

print("Press the enter key to continue.")
print("In a great battle, your shield is destroyed.")
del items[2]
print("Your inventory is now:")
print(items)
print('')

print("Press the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")
del items[:2]
print("Your inventory is now:")
print(items)
