# TV
# Emulation of the TV-chanel

class Television (object):
    """Television emulation class"""
    def __init__(self, name = 'Television',chanel = 1, vol = 10):
        self.name =name
        self.chanel = chanel
        self.vol = vol

    def switch_volume (self,vol):
        print("Current level: ", self.vol, " \n")
        vol_choise = input("Press \"+\" or \"-\" for audio adjustment! ")
        if vol_choise == "+":
            self.vol += 2
        elif vol_choise == "-":
            self.vol -= 2
        else:
            print("Incorrect type!")
        self.volume_controller(vol)
        print("Volume now: ", self.vol, " \n")
        return vol

    def print_program (self, chanel):
        program = ' '
        if chanel < 0 or chanel > 30:
            print("Incorrect number of chanel!")
        elif chanel == 1:
            program = "news"
        elif chanel == 2:
            program = "music"
        elif chanel == 3:
            program = "fun movie"
        elif chanel == 4:
            program = "films"
        elif chanel == 5:
            program = "international news"
        elif chanel == 6:
            program = "tv-shows"
        else:
            program = "unknown"
        print ("You watching ", program, " chanel!")
        return program

    def volume_controller(self,vol):
        if self.vol < 0:
            self.vol = 0
        elif self.vol > 100:
            self.vol = 100
        return vol

def main():
    print("Goog afternoon!\n")
    tv = Television()
    choice = None
    while choice !="0":
        print("""
         What would you like to do:
         0 - Turn off
         1 - Switch chanel
         2 - Change volume
         """)
        choice = input("Your choice: ")
        if choice == "0":
            print("Good bye!")
        elif choice == "1":
            chanel = int(input("Choose your chanel: "))
            tv.print_program(chanel)
        elif choice == "2":
            vol = tv.vol
            tv.switch_volume(vol)
        else:
            print("Incorrect type!!")

main()
input("Press ENTER for exit")
