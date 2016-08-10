from Place import Place
from Being import Being as Being
from Atom import Atom as Atom
from InternalMind import InternalMind as InternalMind
from ExternalMind import ExternalMind as ExternalMind
from Eye import Eye as Eye

# Being : nom, dictin, size, elasticity, visibility, opacity, mind
        
world = Place('world', {
    'dark room': Place('dark room', {
        'goblin': Being('goblin', {
            'body': Atom("body", 5, 5, 0, 5, 0)
        }, 5, 20, 10, 10, InternalMind(1)),
        'cell': Place('cell', {
            'rat': Being('rat', {'body': Atom("body", 5, 5, 0, 5, 0)}, 5, 20, 10, 10,
                         InternalMind(1)),
            'you': Being('you', {'eye': Eye('eye', 1, 1, 0, 1, 0),
                                 'body': Atom("body", 9, 10, 1, 10, 1)}, 10, 20, 10, 7,
                         ExternalMind()),
            'rock': Atom('rock', 1, 10, 1, 10, 10)
        }, 100, 10, 0)
    }, 300, 10, 10)
}, 1000000000000, 0, 0)

you = world.lookfor('you')
while you.act(world) != 'sleep':
    pass
