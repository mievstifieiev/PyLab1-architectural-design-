import Human

class Student(Human.Human):

    def __init__(self, name):
        self._name = name

    def Listen(self, speech):
        print("Student {} listen: {}".format(self._name, speech))
        self.Write(speech)

    def Write(self, speech):
        print("Student {} write: {}".format(self._name, speech))
