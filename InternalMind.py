from Mind import Mind

class InternalMind(Mind): # The computer manage that!
    """Classe caractérisée par :
    - des valeurs de comportement? Agressivité, peur, etc?"""
    
    def __init__(self, agr):
        super(InternalMind, self).__init__()
    def act(self, world, components):
        pass