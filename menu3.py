import pyconio
class MainScreen():
    '''
    A főképernyő objektuma, itt tárolom a főképernyő tulajdonságait.
    Pl. Az egyes menüpontokat stringben, a választási lehetőségek minimumát, maximumát.
    '''
    def __init__(self,):
        self.options = ["Kép betöltése", "Kép átméretezése", "Szín beállítások", "Kép forgatása", "Blur", "Élek kiemelése", "Aktuális kép megjelenítése", "Mentés", "Kilépés"]
        self.MinChoice = 1
        self.MaxChoice = 9

class ScreenOne():
    """
    Az első almenü osztálya, amiben tároljuk a menü tulajdonságait,
    valamint az almenü almenüjei is itt vannak megvalósítva.
    """
    def __init__(self,):
        self.options = ["A teljes elérési út megadása ","Vissza a főmenübe"]
        self.MinChoice = 1
        self.MaxChoice = 2

    def Start(self,currentImg,megnyit,elment):
        while True:
            PrintMenu(self.options)
            option = ValidateInput(self.MinChoice,self.MaxChoice)
            if option == 1:
                flag = False
                if currentImg:
                    PrintMenu(["Már van betöltve egy kép, Kívánod menteni?","Igen","Nem"],0)
                    option = ValidateInput(2,3)
                    if option == 2:
                        PrintMenu(["Adja meg miéyem néven kívánja menteni: "],0)
                        p = input()
                        elment(currentImg,p)
                        flag = True
                try:
                    if flag:
                        p = input("Adja meg az új kép teljes elérési útját: ")
                    else:
                        p = input("Adja meg az elérési utat: ")
                    path = r'{}'.format(p)
                    currentImg = megnyit(path)
                    return currentImg
                except:
                    InvalidInput()
            break

class ScreenTwo():
    """
    A kettes almenü osztálya.
    Csak akkor hozható létre, ha már van betöltött képünk.
    """
    def __init__(self, currentimg):
        self.options = ["A jelenlegi kép méretei {}:{}".format(currentimg.height, currentimg.width), "Százalékosan meghatározott át méretezés, az arányok megtartásával", "Megadott nagyságra skálázás"]
        self.MinChoice = 1
        self.MaxChoice = 4

    def Start(self, currentImg, szazalekos, adottmeret, adottmeretAranyos):
        """
        Ez a függvény indítja el a kettes menüpont almenüjét.
        """
        while True:
            PrintMenu(self.options,0)
            option = ValidateInput(self.MinChoice,self.MaxChoice)
            
            if option == 2:
                PrintMenu(["Adja meg a skálázás mértékét (0.9 => -10%): "],0)
                try:
                    p = float(input())
                    result = szazalekos(currentImg, p)
                    return result
                except:
                    InvalidInput()

            if option == 3:
                PrintMenu(["Adott méretűre skálázás, (Width-Height): ", "Adott méretűre skálázás, (Width-Height) arányok megtartásával: "])
                option = ValidateInput(1,2)
                if option == 1:
                    PrintMenu(["Adja meg az érték(eket) (W:num:H:num)-formában  : "],0)
                    p = input()
                    result = adottmeret(currentImg,p)
                    return result
                elif option == 2:
                    PrintMenu(["Adja meg az értéket (W:num) vagy (H:num) formában: "],0)
                    p = input()
                    result = adottmeretAranyos(currentImg,p)
                    return result

class ScreenThree():
    def __init__(self,):
        self.options = ["RGB TO HVS2", "RGB TO LAB", "Szürke","Vissza a főmenübe"]
        self.MinChoice = 1
        self.MaxChoice = 4

    def Start(self,currentImg):
        while True:
            PrintMenu(self.options)
            option = ValidateInput(self.MinChoice, self.MaxChoice)

            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            else:
                return currentImg
                
class ScreenFour():
    def __init__(self,):
        self.options = ["Kép elforgatása +90", "Kép elforgatása -90", "Kép elforgatása 180", "Vissza főmenübe"]
        self.MinChoice = 1
        self.MaxChoice = 4

    def Start(self, currentImg, rotateLeft, rotateRight, rotate180):
        while True:
            PrintMenu(self.options)
            option = ValidateInput(self.MinChoice, self.MaxChoice)
            if option == 1:
                currentImg = rotateLeft(currentImg)
                return currentImg
            elif option == 2:
                currentImg = rotateRight(currentImg)
                return currentImg
            elif option == 3:
                currentImg = rotate180(currentImg)
                return currentImg
            else:
                return currentImg

class ScreenFive():
    def __init__(self,):
        self.options = ["PIXEL FASZ", "Vissza főmenübe"]
        self.MinChoice = 1
        self.MaxChoice = 2

    def Start(self, currentImg):
        while True:
            PrintMenu(self.options)
            option = ValidateInput(self.MinChoice, self.MaxChoice)
            if option == 1:
                pass
            else:
                return currentImg

class ScreenSix():
    def __init__(self,):
        self.options = []
        self.MinChoice = 1
        self.MaxChoice = 2

    def Start(self,):
        pass

def PrintMenu(options,firsIgnored=None):
    """
    Mivel kiírni az egyes menüket / almenüket nagyon gyakori feladat,
    ezért úgy gondoltam a legjobb kiszervezni ezt egy külön függvénybe.
    
    Egyetlen paramétert fogad: iterálható objektumot ami az egyes menüpontok elemeit tartalmazza =>(str).
    """
    pyconio.clrscr()
    [print("[{}] {}".format(x+1, options[x])) if firsIgnored != x else print("[-] {}".format(options[x])) for x in range(len(options))]

def InvalidInput():
    """
    Pirossal a kiírja, hogy nem megfelelő az input.
    """
    pyconio.textcolor(pyconio.RED)
    print("Nem megfelelő bement, kérem próbálja újra. ")
    pyconio.textcolor(pyconio.WHITE)
    input()

def ImageNotLoaded():
    pyconio.textcolor(pyconio.RED)
    print("Még nem töltött be képállományt, kérem ezzel kezdje.")
    pyconio.textcolor(pyconio.WHITE)
    input() 

def ValidateInput(MinChoice, MaxChoice):
    """
    Sűrűn kell számokat beolvasni és ellenőrizni,
    ezért létrehoztam rá eg függvényt.
    """
    option = input("Adja meg a választott menüpont számát: ")
    try:
        option = int(option)
        if option < MinChoice or option > MaxChoice:
            raise Exception("Nem gut")
        return option
    except:
        InvalidInput()