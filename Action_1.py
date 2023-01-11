

class Action:
    def __init__(self, port):
        self.board = port


    def Action(self , a1 = 0 ,a2 = 0 ,a3 = 0 ,a4  = 0):
        grad = 23 * a1
        grad2 = 110 * a2
        grad3 = 44 * a3
        grad4 = 55 * a4
        done = True
        while done:

            if grad > 0:
                grad -= 1
                self.board.digital[12].write(0)
                self.board.digital[13].write(1)
                self.board.digital[13].write(0)
            elif grad < 0 :
                grad += 1
                self.board.digital[12].write(1)
                self.board.digital[13].write(1)
                self.board.digital[13].write(0)

            if grad2 > 0:
                grad2 -= 1
                self.board.digital[10].write(0)
                self.board.digital[11].write(1)
                self.board.digital[11].write(0)
            elif grad2 < 0 :
                grad2 += 1
                self.board.digital[10].write(1)
                self.board.digital[11].write(1)
                self.board.digital[11].write(0)


            if grad3 > 0:
                grad3 -= 1
                self.board.digital[8].write(1)
                self.board.digital[9].write(1)
                self.board.digital[9].write(0)
            elif grad3 < 0 :
                grad3 += 1
                self.board.digital[8].write(0)
                self.board.digital[9].write(1)
                self.board.digital[9].write(0)


            if grad4 > 0:
                grad4 -= 1
                self.board.digital[6].write(0)
                self.board.digital[7].write(1)
                self.board.digital[7].write(0)
            elif grad4 < 0 :
                grad4 += 1
                self.board.digital[6].write(1)
                self.board.digital[7].write(1)
                self.board.digital[7].write(0)



            # checker mode
            if grad == 0  and grad2 == 0  and grad3 == 0 and grad4 == 0:
                done = False