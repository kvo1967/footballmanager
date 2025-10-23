# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Dutch Football Manager is an intelligent system for the Dutch Eredivisie fantasy league on gratisvoetbalmanager.com. It scrapes player statistics, tracks injuries/suspensions, fetches match odds, and generates comprehensive LLM prompts for AI-powered optimal team selection.

## Running the Application

```bash
# Install dependencies
pip install requests beautifulsoup4

# Set up API key for The Odds API
# Create api-key.txt in project root with your API key from https://the-odds-api.com/

# Run the main application
python main.py
```

The application will:
1. Scrape player data from all 18 Eredivisie clubs
2. Fetch injury/suspension data
3. Match unavailable players using intelligent Dutch name matching
4. Retrieve weekend match odds via The Odds API
5. Prompt for budget input
6. Generate `final_prompt.md` containing a complete LLM prompt with all data

## Architecture

### Main Orchestration (main.py)
Entry point that coordinates the full data collection pipeline:
1. Scrapes players from gratisvoetbalmanager.com
2. Scrapes unavailable players from blessuresenschorsingen.nl
3. Matches unavailable players to fantasy roster using Dutch name parsing
4. Fetches weekend match odds with win probabilities
5. Generates output files and final LLM prompt

### Core Modules

**players/**
- `player.py`: Player class with Dutch name matching logic
  - Handles tussenvoegsels (Dutch middle names: van, de, van der, etc.)
  - Unicode normalization for accents
  - Name format conversion: "Family, I" ↔ "Given Family"
- `matching.py`: Matches unavailable players to roster, returns (available_list, error_list)
- `unavailable.py`: Unavailable player class (injuries/suspensions)
- `import_/`: Web scraping modules
  - `import_players.py`: Scrapes gratisvoetbalmanager.com for player statistics
  - `import_unavailable.py`: Scrapes blessuresenschorsingen.nl for injuries/suspensions
  - `import_constants.py`: Constants for club indices
- `log_/`: File writers for all output files

**matches/**
- `match.py`: Match class with odds data
- `match_writer.py`: Writes weekend matches to file
- `odds_/odds_api_client.py`: The Odds API integration
  - Fetches Eredivisie match odds
  - Converts odds to win probabilities
  - Maps API team names to club registry

**clubs/**
- `club.py`: Club class
- `club_registry.py`: Registry of all 18 Eredivisie clubs with multiple name mappings
  - Each club has: full name, abbreviation, and index
  - Supports name variations (e.g., "Groningen", "FC Groningen")

### Output Files

- `all_players.txt`: Complete player database with statistics
- `unavailable_players.txt`: Injured/suspended players with expected return dates
- `available_players.txt`: Players ready for selection
- `matching_errors.txt`: Unmatched players between fantasy roster and injury list
- `weekend_matches.txt`: Match schedule with win probabilities
- `final_prompt.md`: Complete LLM prompt for team selection

### Fantasy Football Rules

Team selection follows gratisvoetbalmanager.com rules:
- **Formation**: Must use 4-3-3, 4-4-2, 3-5-2, or 3-4-3 (1 keeper + 10 outfield)
- **Club limit**: Maximum 2 players per club
- **Captain**: One player must be captain (receives double points)
- **Budget**: User-defined constraint (default: €115M)

Points system varies by position (K/V/M/A) - see `docs/points_awarded.md` for complete scoring rules.

## Key Implementation Details

### Dutch Name Matching
The name matching algorithm handles:
- Fantasy format: "van Dijk, V"
- News format: "Virgil van Dijk"
- Multi-word tussenvoegsels: "van der", "van de", "van den", "op de", etc.
- Unicode normalization for accented characters
- First initial matching for disambiguation

See `player.py:63` (`matches_unavailable_name`) for implementation.

### API Key Management
The Odds API key must be in `api-key.txt` at project root. The `OddsApiClient` automatically resolves relative paths from the `matches/odds_/` directory.

### Club Registry
All team name variations are normalized through `club_registry`. The odds API uses names like "Ajax Amsterdam" which map to "Ajax" in the registry. See `club_registry.py:26` for all mappings.
