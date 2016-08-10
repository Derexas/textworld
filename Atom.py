from Entity import Entity


class Atom(Entity):  # Plus petite entitée possible. En défini les propriétés
    """Classe caractérisée par :
    - attributs de entity
    - solidité (life)
    - point de détérioration (armor)"""
    def __init__(self, nom, size, visibility, opacity, life, armor):
        super(Atom, self).__init__(nom, {}, size, 0, visibility, opacity)
        self.life = life
        self.armor = armor

    def hit(self, value):
        if value > self.armor:
            self.life -= (value - self.armor)

    def heal(self, value):
        self.life += value

    def exist(self):
        return self.life > 0

    def putentity(self, entity, force):
        print("Can't put anything in an atom")

    def lookfor(self, nom):
        if nom == self.nom:
            return self
        else:
            return False

    def tostring(self):
        return super(Atom, self).tostring() + ' ' + ' '.join(map(str, ['life:', self.life, 'armor:', self.armor]))