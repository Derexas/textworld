from Life import Life
from Atom import Atom


class Eye(Atom, Life):  # Perceive light
    """Classe caractérisée par :
    - attributs de life
    - power or something"""
    def __init__(self, nom, size, visibility, opacity, life, armor):
        super(Eye, self).__init__(nom, size, visibility, opacity, life, armor)
        self.power = 20

    def act(self):
        perception = {}
        self.perceive(self.power, self, perception)
        return perception

    def perceive(self, power, it, perception, scantop=True):
        if power > 20-it.visibility:
            perception[it.nom] = it
            #power -= it.opacity
            if scantop:
                self.perceive(power, it.contenant, perception)
            for name in it.list.keys():
                self.perceive(power, it.list[name], perception, scantop=False)