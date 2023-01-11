


class Reles_action:
    def __init__(self , port):
        ''' Reles harakatini nazorat qilish '''
        self.board = port


    def pozitsion(self ,location ,  next_pozition):
        ''' qaysi joylashuvga borlishi kiritiladi '''
        if next_pozition - location > 0:
            step = (next_pozition - location)*1833
            for _ in range(step):
                self.board.digital[4].write(0)
                self.board.digital[5].write(1)
                self.board.digital[5].write(0)

        if next_pozition - location < 0:
            step_1 = (-1) * (next_pozition-location) * 1833
            for _ in range(step_1):
                self.board.digital[4].write(1)
                self.board.digital[5].write(1)
                self.board.digital[5].write(0)


    def home(self ,  location):
        ''' Ayni vaqtdagi robot joylashuv choragi kiritiladi. '''
        step = (location -1) * 18833
        for _ in range(step):
            self.board.digital[4].write(1)
            self.board.digital[5].write(1)
            self.board.digital[5].write(0)



