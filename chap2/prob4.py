name = input("Hi.  What's your name? ")
age = int(input("And how old are you? "))
weigh = int(input("Okay, last question.  How many pounds do you weigh? "))
print('')

dogYears = int(age / 7)
convertAgeToSec = age * 365 * 24 * 60 * 60
changeName = name * 5
moonWeigh = weigh * (1 / 6)
sunWeigh = weigh * 27.1

print("Did you now that you're just", dogYears, "in dog years?")
print('')
print("But you're also over", convertAgeToSec, "seconds old.")
print('')
print("If a small child were trying to get your attention, your name would become:")
print(changeName)
print('')
print("Did you know that on the moon you would weigh only", moonWeigh, "pounds?")
print("But on the sun, you'd weigh", sunWeigh, "(but, ah... not for long).")
