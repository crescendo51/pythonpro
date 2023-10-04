items = ("sword", "armor", "shield", "healing potion")

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

inputNum = int(input("Enter the index number for an item in inventory: "))
print("At index " + str(inputNum) + " is " + items[inputNum])

print('')
startSliceNum = int(input("Enter the index number to begin a slice : "))
endSliceNum = int(input("Enter the index number to end the slice : "))
print("inventory[ " + str(startSliceNum) + " : " + str(endSliceNum) + " ]\t\t", end = '')
print(items[startSliceNum : endSliceNum])

print('')
print("Press the enter key to continue.")

chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
print(items + chest)
