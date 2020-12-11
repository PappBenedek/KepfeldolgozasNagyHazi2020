import menu3 as menu
import image
currentImg = None

def main(option, currentImg):
    while  option != mc.MaxChoice:
        if option == 1:
            so = menu.ScreenOne()
            currentImg = so.Start(currentImg, image.Img, image.kepMentese)

        elif option == 2:
            if currentImg:
                st = menu.ScreenTwo(currentImg)
                currentImg = st.Start(currentImg, image.szazalekosAtmeretezes, image.adottMeretuKep, image.adottMeretKepAranyokMegtartasaval)
            else:
                menu.ImageNotLoaded()

        elif option == 3:
            if currentImg:
               sth = menu.ScreenThree()
               currentImg = sth.Start(currentImg, image.rgbToHvs, image.rgbToLab, image.rgbToGrey)
            else:
                menu.ImageNotLoaded()
        elif option == 4:
            sf = menu.ScreenFour()
            sf.Start(currentImg, image.forgatas90FokkalBalra, image.forgatas90FokkalJobbra, image.forgatas180FokkalBalra)
        elif option == 5:
            scf = menu.ScreenFive()
            scf.Start(currentImg, image.blur)
        elif option == 6:
            ss = menu.ScreenSix()
            ss.Start(currentImg, image.elekKeresese)
        elif option == 7:
            image.kepMegjelelitese(currentImg)

        elif option == 8:
            se = menu.ScreenEight()
            se.Start(currentImg, image.kepMentese)

        menu.PrintMenu(mc.options)
        option = menu.ValidateInput(mc.MinChoice, mc.MaxChoice)




mc = menu.MainScreen()
menu.PrintMenu(mc.options)
option = menu.ValidateInput(mc.MinChoice,mc.MaxChoice)
main(option,currentImg)  
