import uuid


# Maybe use chainmap for the zoo?


class Animal:
    def __init__(
        self,
        name: str,
        species: str,
        required_space: int,
        predator: bool,
        legs: int,
        color: str,
    ):
        self.name = str(name)
        self.species = str(species)
        self.required_space = int(required_space)
        self.predator = bool(predator)
        self.legs = int(legs)
        self.color = str(color)

    def __iter__(self):
        return (
            i
            for i in (
                self.name,
                self.species,
                self.required_space,
                self.predator,
                self.legs,
                self.color,
            )
        )

    def __str__(self):
        return "".join([(f"{key}: {value}\n") for key, value in vars(self).items()])

    def __repr__(self):
        class_name = type(self).__name__
        attributes = ", ".join(
            [(f"{key}={value!r}") for key, value in vars(self).items()]
        )
        return f"{class_name}({attributes})"


wolf = Animal("Wolf", "Canis lupus", 20, True, 4, "grey")
print(wolf)
print(repr(wolf))

owl = Animal("Owl", "Strigiformes", 5, True, 2, "brown")
print(owl)

rabbit = Animal("Rabbit", "Bunnyus fuzzyus", 10, False, 4, "white")


class Cage:
    def __init__(self, name, size=60, animals: list = None):
        self.name = str(name)
        self.size = int(size)
        self.animals = animals if animals else list()
        self.id = uuid.uuid4()
        self.empty_space = self.size

    def __iter__(self):
        return (i for i in (self.animals))

    def __repr__(self):
        class_name = type(self).__name__
        attributes = ", ".join(
            [(f"{key}={value!r}") for key, value in vars(self).items()]
        )
        return f"{class_name}({attributes})"

    def __str__(self):
        animals_str = "".join(f"{i}\n" for i in self.animals)
        return f"{self.name} has these animals:\n{animals_str}"

    def add_animals(self, *animals):
        for animal in animals:
            if self.animals is None:
                self.animals = []

            if animal.required_space > self.empty_space:
                print(
                    f"Not enough space for a new {animal.name}. "
                    f"Remaining space is {self.empty_space} sq meters. "
                    f"Your animal requires {animal.required_space} sq meters"
                )
                return

            if not all(a.predator == animal.predator for a in self.animals):
                conflicting_animals = ", ".join([a.name for a in self.animals])
                print(
                    f"You can't put a {animal.name} in this cage. \n"
                    f"The cage currently has animals with different predatory behavior.\n"
                    f"They are: {conflicting_animals}"
                )
                return

            self.empty_space -= animal.required_space
            self.animals.append(animal)
            print(
                f"{animal.name} added. f{self.empty_space} sq meters remain in this cage."
            )


forest_cage = Cage("forest_cage")
forest_cage.add_animals(wolf)
forest_cage.add_animals(wolf)
forest_cage.add_animals(wolf)
forest_cage.add_animals(wolf)

aviary = Cage("aviary", 40, [owl, owl, owl])
aviary.add_animals(rabbit)


class Zoo:
    def __init__(self, name, cages: list = None):
        self.cages = cages if cages else list()
        self.name = str(name)

    def __iter__(self):
        return (i for i in self.cages)

    def __repr__(self):
        class_name = type(self).__name__
        attributes = ", ".join(
            [(f"{key}={value!r}") for key, value in vars(self).items()]
        )
        return f"{class_name}({attributes})"

    def __str__(self):
        cages_str = "".join(f"{i} \n" for i in self.cages)
        return f"{self.name} has these cages:\n{cages_str}"

    def animals_by_color(self, color: str):
        color_list = [
            animal
            for cage in self.cages
            for animal in cage.animals
            if animal.color == color
        ]
        return color_list

    def animals_by_legs(self, legs: int):
        leg_list = [
            animal
            for cage in self.cages
            for animal in cage.animals
            if animal.legs == legs
        ]
        return leg_list
    
    
    def animals_by_keyword(self, **kwargs):
        matching_animals = []

        for cage in self.cages:
            for animal in cage.animals:
                if any(hasattr(animal, key) and getattr(animal, key) == value for key, value in kwargs.items()):
                    matching_criteria = ", ".join(f"{key}={value}" for key, value in kwargs.items())
                    matching_animals.append(f'{matching_criteria}: \n{animal}')

        if not matching_animals:
            return "No animals match any of the traits you searched for."

        animal_str = ''.join(f'{i}\n' for i in matching_animals)
        return f'These animals match at least one of the traits you searched for:\n{animal_str}'

    def number_of_legs(self):
        return sum(animal.legs for cage in self.cages for animal in cage.animals)


small_zoo = Zoo("silly_zoo", [forest_cage, aviary])
print(str(small_zoo))
print()
print(small_zoo.animals_by_color("brown"))
print()
print(small_zoo.animals_by_legs(4))
print()
print(small_zoo.number_of_legs())
print()
print(small_zoo.animals_by_keyword(color='brown', legs=4))
print()
# print(small_zoo.animals_by_keyword(legs=4))