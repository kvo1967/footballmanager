from .club import Club

class ClubRegistry:
    def __init__(self):
        self.clubs = [
            Club("Ajax", "AJAX", 2),
            Club("AZ", "AZ", 3),
            Club("Excelsior", "EXC", 22),
            Club("Feyenoord", "FEY", 9),
            Club("Fortuna Sittard", "FOR", 27),
            Club("Go Ahead Eagles", "GAE", 19),
            Club("FC Groningen", "GRO", 5),
            Club("SC Heerenveen", "HEE", 15),
            Club("Heracles Almelo", "HER", 10),
            Club("NAC Breda", "NAC", 11),
            Club("NEC", "NEC", 12),
            Club("PEC Zwolle", "PEC", 4),
            Club("PSV", "PSV", 13),
            Club("Sparta Rotterdam", "SPA", 25),
            Club("Telstar", "TEL", 31),
            Club("FC Twente", "TWE", 6),
            Club("FC Utrecht", "UTR", 7),
            Club("FC Volendam", "VOL", 29)
        ]

        self.name_mapping = {
            "ajax": self.clubs[0],
            "az": self.clubs[1],
            "excelsior": self.clubs[2],
            "feyenoord": self.clubs[3],
            "fortuna sittard": self.clubs[4],
            "go ahead eagles": self.clubs[5],
            "fc groningen": self.clubs[6],
            "groningen": self.clubs[6],
            "heerenveen": self.clubs[7],
            "sc heerenveen": self.clubs[7],
            "heracles": self.clubs[8],
            "heracles almelo": self.clubs[8],
            "nac breda": self.clubs[9],
            "nac": self.clubs[9],
            "nec": self.clubs[10],
            "pec zwolle": self.clubs[11],
            "pec": self.clubs[11],
            "psv": self.clubs[12],
            "sparta rotterdam": self.clubs[13],
            "sparta": self.clubs[13],
            "telstar": self.clubs[14],
            "fc twente": self.clubs[15],
            "twente": self.clubs[15],
            "fc utrecht": self.clubs[16],
            "utrecht": self.clubs[16],
            "fc volendam": self.clubs[17],
            "volendam": self.clubs[17]
        }

        self.index_mapping = {club.index: club for club in self.clubs}

    def get_by_name(self, name):
        name_lower = name.lower().strip()
        return self.name_mapping.get(name_lower)

    def get_by_index(self, index):
        return self.index_mapping.get(index)

    def get_all_clubs(self):
        return self.clubs.copy()

club_registry = ClubRegistry()