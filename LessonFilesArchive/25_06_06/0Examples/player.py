# Class to be imported and used across many programs

class Player:
    def __init__(self, name, team, nationality, position):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.position = position

    def to_dict(self):
        return {
            "name": self.name,
            "team": self.team,
            "nationality": self.nationality,
            "position": self.position
            }

    @staticmethod
    def load_from_dict(p_dict : dict[str,str]):
        return Player(p_dict["name"],p_dict["team"],p_dict["nationality"],p_dict["position"])

    def __repr__(self):
        return self.name