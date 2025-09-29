# Dutch Football Manager 🏆⚽

An intelligent football manager system for the Dutch Eredivisie that generates data-driven LLM prompts for optimal team selection on [gratisvoetbalmanager.com](https://www.gratisvoetbalmanager.com).

## Features

- **Player Data Scraping**: Automatically collects comprehensive player statistics from all 18 Eredivisie clubs
- **Injury/Suspension Tracking**: Monitors player availability with intelligent Dutch name matching
- **Real-time Match Odds**: Integrates weekend match probabilities via The Odds API
- **LLM Prompt Generation**: Creates comprehensive prompts for AI-powered team selection
- **Budget Management**: Handles user-defined budget constraints for team composition

## How It Works

1. **Data Collection**: Scrapes player performance data from gratisvoetbalmanager.com
2. **Availability Check**: Cross-references with injury/suspension data from blessuresenschorsingen.nl
3. **Match Analysis**: Fetches weekend match odds and win probabilities
4. **Prompt Creation**: Generates a complete LLM prompt with all data for optimal team selection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kvo1967/footballmanager.git
cd footballmanager
```

2. Install required dependencies:
```bash
pip install requests beautifulsoup4
```

3. Set up your API key:
   - Get a free API key from [The Odds API](https://the-odds-api.com/)
   - Create `api-key.txt` in the project root
   - Paste your API key in the file

## Usage

Run the main script:
```bash
python main.py
```

The program will:
1. Scrape all player data from 18 Eredivisie clubs
2. Check for injuries and suspensions
3. Fetch weekend match odds
4. Ask for your budget (in millions €)
5. Generate a comprehensive LLM prompt in `final_prompt.md`

## Project Structure

```
footballmanager/
├── main.py                     # Main orchestration script
├── players/
│   ├── player.py              # Player class with Dutch name matching
│   ├── matching.py            # Available players calculation
│   ├── import_/               # Data collection modules
│   └── log_/                  # File output writers
├── matches/
│   ├── match.py               # Match class
│   ├── match_writer.py        # Match data output
│   └── odds_/                 # Odds API integration
├── clubs/
│   ├── club.py                # Club class
│   └── club_registry.py       # 18 Eredivisie clubs registry
└── docs/
    ├── basic_prompt.md         # LLM prompt template
    ├── game_rules.md          # Fantasy football rules
    └── points_awarded.md      # Scoring system
```

## Output Files

The program generates several output files:
- `all_players.txt` - Complete player database
- `unavailable_players.txt` - Injured/suspended players
- `available_players.txt` - Players ready for selection
- `weekend_matches.txt` - Match schedule with odds
- `final_prompt.md` - Complete LLM prompt for team selection

## Game Rules

The system follows [gratisvoetbalmanager.com](https://www.gratisvoetbalmanager.com) rules:
- **Team size**: Exactly 11 players
- **Club limit**: Maximum 2 players per club
- **Captain required**: One player must be designated as captain (double points)
- **Budget constraint**: User-defined total budget
- **Formation**: Choose from 4-3-3, 4-4-2, 3-5-2, or 3-4-3

## Features Highlights

### Intelligent Name Matching
Handles complex Dutch name variations:
- Fantasy format: "van Dijk, V"
- News format: "Virgil van Dijk"
- Supports tussenvoegsels (Dutch middle names)
- Unicode normalization for accents

### Real-time Data Integration
- Live player statistics
- Current injury/suspension status
- Weekend match odds and probabilities
- Dynamic team name mapping

### LLM-Ready Output
Generates comprehensive prompts including:
- All game rules and constraints
- Player statistics and availability
- Match probabilities for strategic decisions
- Budget optimization guidelines

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for educational and personal use. Please respect the terms of service of the websites being scraped and the APIs being used.

----------------------------------------------------------------------

*Generated with ❤️ and [Claude Code](https://claude.ai/code)*