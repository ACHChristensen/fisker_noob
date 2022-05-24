class Fish():

    def __init__(self, species, characteristics, poisen, minimal_size, closed_for_season = [], target_value=None):
        self.species= species
        self.characteristics = characteristics
        self.poisen = poisen
        self.minimal_size = minimal_size
        self.closed_for_season = closed_for_season
        self.target_value = target_value
    
    @property
    def fish(self):
        return self.fish

#    @fish.setter
#    def set_
        