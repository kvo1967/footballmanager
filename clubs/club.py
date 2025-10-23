class Club:
    """
    Purpose: hold club information to hold player-club relationship
    """
    def __init__(self, name, short_name, index):
        self.name = name
        self.short_name = short_name
        self.index = index

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Club('{self.name}', '{self.short_name}', {self.index})"