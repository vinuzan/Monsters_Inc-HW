class Monsters():
    #Characteristics
    def __init__(self, name, eye, fur, cuteness, skills):
        self.name = name
        self.eye = eye
        self.fur = fur
        self.cuteness = False
        self.skills = skills

    #Methods
    def scare(self):
        return 'Rahhh Raahh'
    def eat(self):
        return 'NOM NOM'
    def transform(self):
        return 'zoommm'
    def hide(self):
        return 'peakaboo'
    def sleep(self):
        return 'Zzzzz'
    def hobby(self):
        return 'ahahaha'