import unicodedata

class Player:
    def __init__(self, position, name, price, played, won, draw, lost, goals_for, goals_against, clean_sheet, assist, yellow, red, og, score, club):
        self.position = position          # Player's position on the field (e.g., Forward, Midfielder)
        self.name = name                  # Player's full name
        self.price = price                # Player's market value or cost
        self.played = played              # Number of matches played
        self.won = won                    # Number of matches won
        self.draw = draw                  # Number of matches drawn
        self.lost = lost                  # Number of matches lost
        self.goals_for = goals_for        # Goals scored by the player
        self.goals_against = goals_against  # Goals conceded while the player was on the field
        self.clean_sheet = clean_sheet    # Matches with no goals conceded
        self.assist = assist              # Number of assists made by the player
        self.yellow = yellow              # Number of yellow cards received
        self.red = red                    # Number of red cards received
        self.og = og                      # Number of own goals
        self.score = score                # Total score (e.g., fantasy points, performance index)
        self.club = club                  # Player's club object

    @staticmethod
    def normalize_text(text):
        """
        Normalize text by removing accents/diacritics and converting to lowercase
        """
        normalized = unicodedata.normalize('NFD', text)
        ascii_text = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
        return ascii_text.lower().strip()

    @staticmethod
    def extract_family_name(name_parts):
        """
        Extract family name including Dutch middle names (tussenvoegsels)
        """
        dutch_middle_names = {
            'van der', 'van de', 'van den', 'van het', 'van', 'de', 'den', 'der',
            '\'t', 'van \'t', 'el', 'al', 'ten', 'ter', 'te', 'op de', 'op den', '\´t'
        }

        if len(name_parts) < 2:
            return name_parts[-1] if name_parts else ""

        family_parts = []
        i = 1
        while i < len(name_parts):
            current_part = name_parts[i]

            for middle_name in sorted(dutch_middle_names, key=len, reverse=True):
                middle_parts = middle_name.split()
                if i + len(middle_parts) - 1 < len(name_parts):
                    candidate = ' '.join(name_parts[i:i + len(middle_parts)])
                    if candidate == middle_name:
                        family_parts.extend(name_parts[i:i + len(middle_parts)])
                        i += len(middle_parts)
                        break
            else:
                family_parts.append(current_part)
                i += 1

        return ' '.join(family_parts) if family_parts else name_parts[-1]

    def matches_unavailable_name(self, unavailable_name):
        """
        Check if this player matches an unavailable player name
        """
        unavailable_norm = Player.normalize_text(unavailable_name)
        player_norm = Player.normalize_text(self.name)

        unavailable_parts = unavailable_norm.split()
        if len(unavailable_parts) < 2:
            return False

        given_name = unavailable_parts[0]
        family_name = Player.extract_family_name(unavailable_parts)

        if player_norm.startswith(family_name + ","):
            initials_part = player_norm.split(",", 1)[1].strip()
            if initials_part and initials_part[0] == given_name[0]:
                return True

        return False