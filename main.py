import menu3 as menu
import image
#valami
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
               currentImg = sth.Start(currentImg)
            else:
                menu.ImageNotLoaded()
        elif option == 4:
            sf = menu.ScreenFour()
            sf.Start(currentImg, image.forgatas90FokkalBalra, image.forgatas90FokkalJobbra, image.forgatas180FokkalBalra)
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            image.kepMegjelelitese(currentImg)

        elif option == 8:
            image.kepMentese(currentImg, "valamiúj")





        menu.PrintMenu(mc.options)
        option = menu.ValidateInput(mc.MinChoice, mc.MaxChoice)




mc = menu.MainScreen()
menu.PrintMenu(mc.options)
option = menu.ValidateInput(mc.MinChoice,mc.MaxChoice)
main(option,currentImg)  
