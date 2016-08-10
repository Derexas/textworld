from Entity import Entity


class Place(Entity):  # A place, like a cell or a city
    """Classe caractérisée par :
    - attributs de entity
    - position"""
    def __init__(self, nom, dictin, size, visibility, opacity):  #, position):
        super(Place, self).__init__(nom, dictin, size, 0, visibility, opacity)