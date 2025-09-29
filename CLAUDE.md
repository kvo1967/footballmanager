# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Football manager application for tracking player statistics and performance.

## Architecture

- **main.py**: Entry point that imports and uses player data gathering functionality
- **players/**: Module for player-related functionality
  - **player.py**: Player class definition with attributes for position, name, price, match statistics (played, won, draw, lost), performance metrics (goals_for, goals_against, no_goal, assist), disciplinary records (yellow, red, og), and score
  - **import/**: Directory for player data import functionality

## Running the Application

```bash
python main.py
```