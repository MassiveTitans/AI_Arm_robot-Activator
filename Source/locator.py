import Reles_action




class Locator:
    '''  Arm robotni pozitsiyalar aro harakatini taminlaydi  '''
    def __init__(self, port):
        self.port = port


    def locator(self ,location, y ,x ):
        rel = Reles_action.Reles_action(port=self.port)
        if 360 < y:
            if 280 < x < 490:
                rel.pozitsion(location , 1)

            elif 490 < x < 700:
                rel.pozitsion(location, 2)

            elif 700 < x < 910:
                rel.pozitsion(location, 3)

            elif 910 < x < 1120:
                rel.pozitsion(location, 4)

        elif 360 > y:
            if 280 < x < 490:
                rel.pozitsion(location, 1)

            elif 490 < x < 700:
                rel.pozitsion(location, 2)

            elif 700 < x < 910:
                rel.pozitsion(location, 3)

            elif 910 < x < 1120:
                rel.pozitsion(location, 4)


    def poz(self , x ):
        global pozition
        pozition = 0

        if 280 < x < 490:
            pozition = 1

        elif  490 < x < 700:
            pozition = 2

        elif  700 < x < 910:
            pozition  = 3

        elif  910 < x < 1120:
            pozition = 4

        return pozition


    def left_right(self ,  y):
        if y < 360:
            return 0

        if y > 360:
            return 1