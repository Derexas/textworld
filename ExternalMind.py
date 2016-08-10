from Mind import Mind

command = {
    'help': 'Show you this',
    'sleep': 'Quit the world',
    'look [x]': "Describe x if it's visible",
    'put [x] in [y]': 'Move a visible entity to another, if possible',
    'hit [x]': 'Hit a visible entity, potentially causing damages'
}


class ExternalMind(Mind):  # (User controlled)
    """Classe caractérisée par :
    - nothing at all? Abstract class maybe?(If possible)
    - recipent (being)"""
    """Some input methods or something"""
    n = 0
    actions = {}

    def __init__(self):
        super(ExternalMind, self).__init__()
        ExternalMind.n += 1
        def help():
            for name in command.keys():
                print(name+" : "+command[name])
        self.actions['help'] = [0, help]
        def look(target):
            if 'eye' in self.recipient.list:
                perception = self.recipient.list['eye'].act()
                print(perception)
                if target in perception.keys():
                    lookresult = perception[target]
                    if lookresult:
                        lookresult.print()
                else:
                    print(target+" does not exist or is not visible")
            else:
                print("You can't do that because you have no eyes")
        self.actions['look'] = [1, look]
        def hit(target):
            e1 = self.recipient.contenant.lookfor(target)
            if e1:
                e1.hit(2)
                print(target+" has been hit")
            else:
                print(target+" does not exist or is not visible")
        self.actions['hit'] = [1, hit]
        def put(target1, placement, target2, force_boolean):
            if placement == 'in':
                e1 = self.recipient.contenant.lookfor(target1)
                e2 = self.recipient.contenant.lookfor(target2)
                if e1 and e2:
                    if e2.putentity(e1, force_boolean):
                        print(e1.nom+" has been put in "+e2.nom)
                    else:
                        print(e1.nom+" is too big for being in "+e2.nom)
            else:
                print(placement+" is not defined")
        self.actions['put'] = [3, put, False]
        self.actions['force'] = [3, put, True]

    def act(self, world, being):
        str = input("What do you do ? ")
        str = str.replace('around', being.contenant.nom)
        str = str.split(" ")
        if str[0] in self.actions:
            action = self.actions[str[0]]
            args = str[1:]
            if len(args) == action[0]:
                args = args + action[2:]
                action[1](*args)
        elif str[0] != 'sleep':
            print("i'm afraid you can't do that")
        return action[0]