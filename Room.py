
class Room:

    humans = []
    teacher = object

    def __init__(self, humans, teacher):
        self.humans = humans
        self.teacher = teacher

    def Start_lection(self):
        self.teacher.Speak(self)

    def Sound_Propagation(self, speech):
        for human in self.humans:
            human.Listen(speech)