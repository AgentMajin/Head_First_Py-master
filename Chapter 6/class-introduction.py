class Athlete:
    def __init__(self,value = 0):
        print(self)
        self = value
        print(self)

    def how_big(self):
        print(self)

d = Athlete("Holly Grail")
d.how_big()