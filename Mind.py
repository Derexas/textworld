class Mind: # What is an mind? We will try to answer that
    """Classe caractérisée par :
    - memory of perceptions"""
    # I think we can make something like setting some values relatively
    # to the action of the user/computer, and then make the entity act
    # according to them, readin it's 'Mind'
    def __init__(self):
        self.memory = {}
        self.recipient = False
    def act(self, components):
        pass
    def setrecipient(self, being):
        self.recipient = being