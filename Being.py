from Life import Life


class Being(Life):  # Entitée pouvant agir, faire des choix, etc
    """Classe caractérisée par :
    - attributs de life
    - intelligence (Mind)"""
    def __init__(self, nom, dictin, size, elasticity, visibility, opacity, mind):
        super(Being, self).__init__(nom, dictin, size, elasticity, visibility, opacity)
        self.mind = mind
        self.mind.setrecipient(self)

    def act(self, world):
        return self.mind.act(world, self)