class Critter() :
    mood_level = 0
    
    def __init__(self, name) :
        self.name = name

    def setMood(level) : 
        Critter.mood_level += level
    
    def getMood() :
        return Critter.mood_level

    def talk(self) :
        if Critter.getMood() <= 2 :
            print("I'm " + self.name + " and I feel mad now")
            print('')
            Critter.setMood(-1)

        elif Critter.getMood() <= 4 :
            print("I'm " + self.name + " and I'm doing okay")
            print('')
            Critter.setMood(-1)
        
        elif Critter.getMood() <= 6 :
            print("I'm " + self.name + " and I feel happy now")
            Critter.setMood(-1)

        else :
            print("I'm " + self.name + " and I feel overjoyed now")
            Critter.setMood(-1)

    def feed(self) :
        print("Yummy!")
        print('')
        Critter.setMood(2)

    def play(self) :
        print("Wheee!")
        print('')
        Critter.setMood(2)

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
        crit.feed()
    elif choice == 3 :
        crit.play()
