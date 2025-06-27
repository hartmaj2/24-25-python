class Country:
    
    def __init__(self):
        self.name : str = ""
        self.capital : str = ""
        self.population : int = -1

    def __repr__(self):
        return f"{self.name:30}{self.capital:15}{self.population:,}"