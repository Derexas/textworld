import random


class Entity:  # Définition de la classe Entity (Mère du reste)
    """Classe caractérisée par :
    - nom
    - liste d'autres entity contenues
    - entity contenant
    - position dans l'entitée contenant (précis? général?)
    - taille (précis? général?)
    - visibilitée
    - opacité"""
# Eh I put myself so you know I'm important!
# What about trashing that destroyable Atom logic, and put the more logic
# indestructible Atom and structurably breakable entity ? Because it seems neat
# Or maybe not, it's not an atomic simulator
    def __init__(self, nom, dictin, size, elasticity, visibility, opacity):  # Le constructeur
        self.nom = nom
        self.size = size
        self.freespace = size
        self.elasticity = elasticity
        self.visibility = visibility
        self.opacity = opacity
        self.list = {}
        for name in dictin.keys():
            self.putentity(dictin[name], True)

    def exist(self):  # Retourne un boolean d'existence
        for entity in list:
            if not entity.exist():
                return False
        return True

    def putentity(self, entity, force):
        freespace = self.freespace + (self.size * self.elasticity/100) if force else 0
        print("freespace:", freespace, "size:", entity.size)
        if entity.size <= freespace:
            if hasattr(entity, 'contenant'):
                del entity.contenant.list[entity.nom]
            self.list[entity.nom] = entity
            entity.contenant = self
            self.freespace -= entity.size
            return True
        else:
            return False

    def hit(self, value):
        self.list[random.choice(list(self.list.keys()))].hit(value)

    def lookfor(self, nom):
        if nom == self.nom:
            return self
        for name in self.list.keys():
            if name == nom:
                return self.list[name]
            lookresult = self.list[name].lookfor(nom)
            if lookresult:
                return lookresult
        print(len(self.list))
        return False

    def tostring(self):
        return ' '.join(map(str, [self.nom, 'size:', self.size, 'elasticity:', self.elasticity, 'visibility:', self.visibility, 'opacity:', self.opacity]))

    def print(self, dist=""):
        print(dist + self.tostring(), "with")
        for name in self.list.keys():
            self.list[name].print(dist+"  ")
