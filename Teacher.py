import Human

class Teacher(Human.Human):

    def __init__(self, name):
        self._name = name

    def Listen(self, speech):
        pass

    def Speak(self, room):
        speech = input("The {} says: ".format(self._name))
        room.Sound_Propagation(speech)
