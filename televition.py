# TV
# Emulation of the TV-chanel

class Television (object):
    """Television emulation class"""
    def __init__(self, name = 'Television',chanel = 1, vol = 20):
        self.name =name
        self.chanel = chanel
        self.vol = vol

    def switch_volume (self,vol):
        vol_choise = input("Press \"+\" or \"-\" for audio adjustment! ")
        if vol_choise == "+":
            vol += 2
            print("Volume increased to ",vol,"!")
        elif vol_choise == "-":
            vol -= 2
            print("Volume down to ",vol,"!")
        else:
            print("Incorrect type!")
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
            print("Current level: ", vol, " \n")
            tv.switch_volume(vol)
            if vol < 0:
                tv.vol = 0
            elif vol > 100:
                tv.vol = 100
        else:
            print("Incorrect type!!")

main()
input("Press ENTER for exit")
