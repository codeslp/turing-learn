import uuid
from typing import Optional


# Maybe use chainmap for the zoo?

class Animal:
    def __init__(self, name: str, species: str, required_space: int, 
                 predator: bool):
        self.name = str(name)
        self.species = str(species)
        self.required_space = int(required_space)
        self.predator = bool(predator)

    def __iter__(self):
        return(i for i in (self.name, self.species, self.required_space, 
                           self.predator))

    def __str__(self):
        return ''.join([(f'{key}: {value}\n') for key, value in vars(self).items()])
        
    def __repr__(self):
        class_name = type(self).__name__
        attributes = (', '.join([(f'{key}={value!r}') for key, value in vars(self).items()]))
        return f'{class_name}({attributes})'

wolf = Animal('Wolf', 'Canis lupus', 20, True)
print(wolf)
print(repr(wolf))


class Cage:
    def __init__(self, iterable):
        self.size = 60
        self.animals = Optional[list(iterable)]
        self.id = uuid.uuid4()


    

    