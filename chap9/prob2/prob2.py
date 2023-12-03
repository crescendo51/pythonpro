class Critter :
    mood_level = 0
    
    def __init__(self, name) :
        self.name = name

    def setMood(self, level) : 
        Critter.mood_level += level
    
    def getMood(self) :
        return Critter.mood_level

    def talk(self) :
        mood = self.getMood()
        if mood <= 2 :
            print("I'm " + self.name + " and I feel mad now")

        elif mood <= 4 :
            print("I'm " + self.name + " and I'm doing okay")
        
        elif mood <= 6 :
            print("I'm " + self.name + " and I feel happy now")

        else :
            print("I'm " + self.name + " and I feel overjoyed now")
        print('')
        self.setMood(-1)

    def feed(self, food) :
        print("Yummy!")
        print('')
        self.setMood(food.getLevel())

    def play(self) :
        print("Wheee!")
        print('')
        self.setMood(2)

class Food :
    def __init__(self, name, level) :
        self.name = name
        self.level = level

    def getLevel(self) :
        return self.level

    def setCritterLevel(self, critter) :
        critter.setMood(critter.getMood() + self.level)


food1 = Food("feed", 1)
food2 = Food("meat", 3)
food3 = Food("vegetable", 2)

input_name = input("What do you want to name your critter?: ")
print('')

crit = Critter(input_name)
while True :
    print("\tCritter Caretaker")
    print('')
    print("\t0 - Quit")
    print("\t1 - Listen to your critter")
    print("\t2 - Feed your critter")
    print("\t3 - Play with your critter")
    print('')
    choice = int(input("Choice: "))
    if choice == 0 :
        break
    elif choice == 1 :
        crit.talk()
    elif choice == 2 :
        print("\tChoose food for your critter")
        print("\t0 - feed")
        print("\t1 - meat")
        print("\t2 - vegetable")
        foodChoice = int(input("\tWhat kind of food would you feed your pet? : "))
        if foodChoice == 0 :
            crit.feed(food1)
        elif foodChoice == 1 :
            crit.feed(food2)
        elif foodChoice == 2 :
            crit.feed(food3)
    elif choice == 3 :
        crit.play()
