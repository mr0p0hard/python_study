# TV
# Emulation of the TV-chanel
class Critter (object):
    """Television emulation class"""
    def __init__(self, name, chanel = 1, volume = 20):
        self.name = name
        self.chanel = chanel
        self.volume = volume
        
    @switch_chanel.setter
    def switch_chanel (self):
        program = ' '
        if self.chanel < 0 or self.chanel > 30:
            print("Incorrect number of chanel!")
        elif self.chanel == 1:
            program = "news"
        elif self.chanel == 2:
            program = "music"
        elif self.chanel == 3:
            program = "fun movie"
        elif self.chanel == 4:
            program = "films"
        elif self.chanel == 5:
            program = "international news"
        elif self.chanel == 6:
            program = "tv-shows"
        else:
            program = "unknown"
        print ("You watching ", program, " chanel!")
        return self.chanel

    @property
    def switch_volume (self):
        vol = self.volume
        print ("Current level: ", vol, " \n")
        choise = input("Press \"+\" or \"-\" for audio adjustment! ")
        if choise == "+":
            self.volume += 2
        elif choise == "-":
            self.volume -= 2
        else:
            print("Incorrect type!")
        if self.volume < 0:
            self.volume = 0
        elif self.volume > 100:
            self.volume = 100

def main():
    print("Goog afternoon!\n")
    tv_chanel = int(input("What chanel you want to watch? "))
    tv = Critter(tv_chanel)
    choice = None
    while choice !="0":
        print \
        ("""
         What would you like to do:
         0 - Turn off
         1 - Switch chanel
         2 - Change volume
         """)
        choice = input("Your choice: ")
        if choice == "0":
            print("Good bye!")
        elif choice == "1":
            tv.switch_chanel()
        elif choice == "2":
            tv.switch_volume()
        else:
            print("Incorrect type!!")

main()
input("Press ENTER for exit")
