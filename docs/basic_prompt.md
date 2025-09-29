# Taak
Stel het optimale elftal samen voor gratisvoetbalmanager.com op basis van de spelregels en beschikbare spelersinformatie.
Temperatuur: 0.3

# Spelregels en Beperkingen

## Basisregels:
- **Teamgrootte**: Het elftal moet uit precies 11 spelers bestaan
- **Clubbeperking**: Maximaal 2 spelers van dezelfde club
- **Aanvoerder verplicht**: Er moet altijd een aanvoerder (C) worden aangewezen
- **Budget**: Totaal budget van €[XXX] miljoen voor alle 11 spelers
- **Formatie**: Formatie één van (4-3-3, 4-4-2, 3-5-2, 3-4-3.)

## Puntensysteem:
- Spelers krijgen punten op basis van hun prestaties in echte wedstrijden
- De aanvoerder krijgt **dubbele punten** (zowel positieve als negatieve)

## Puntentelling per positie
### K (Keeper)
Wedstrijd gewonnen = 3
Wedstrijd gelijk = 1
Wedstrijd verloren = 0
Gemaakt doelpunt = 10
Assists = 5
Geel = -2
Rood = -3
Eigen doelpunt = -3
De nul = 4
Basis speler = 2
Invaller = 1
Tegen doelpunt = -2

### V (Verdediger)
Wedstrijd gewonnen = 3
Wedstrijd gelijk = 1
Wedstrijd verloren = 0
Gemaakt doelpunt = 5
Assists = 3
Geel = -2
Rood = -3
Eigen doelpunt = -3
De nul = 3
Gespeeld = 0
Basis speler = 2
Invaller = 1
Tegen doelpunt = -1

### M (Middenvelder)
Wedstrijd gewonnen = 3
Wedstrijd gelijk = 1
Wedstrijd verloren = 0
Gemaakt doelpunt = 4
Assists = 2
Geel = -1
Rood = -3
Eigen doelpunt = -4
De nul = 0
Basis speler = 2
Invaller = 1
Tegen doelpunt = 0

### A (Aanvaller)
Wedstrijd gewonnen = 3
Wedstrijd gelijk = 1
Wedstrijd verloren = 0
Gemaakt doelpunt = 3
Assists = 3
Geel = -1
Rood = -3
Eigen doelpunt = -5
De nul = 0
Basis speler = 2
Invaller = 1
Tegen doelpunt = 0


## Strategie voor Elftal Samenstelling

### Prioriteiten (in volgorde van belangrijkheid):
1. **Aanvoerderskeuze**: Selecteer de speler met het hoogste verwachte puntenpotentieel als aanvoerder vanwege de dubbele punten
2. **Budgetoptimalisatie**: Maximaliseer de verwachte punten binnen het budget van €[XXX] miljoen
3. **Risicospreiding**: Verdeel spelers over verschillende clubs (max 2 per club)
4. **Positiebalans**: Zorg voor een realistische en gebalanceerde formatie

### Te overwegen factoren:
- **Speeltijd**: Geef prioriteit aan vaste basisspelers
- **Vorm**: Huidige vorm en fitnesswaarde van spelers
- **Wedstrijdschema**: Aantal verwachte wedstrijden in de aankomende periode
- **Prijs-prestatieverhouding**: Zoek spelers met hoge puntverwachting, maw van teams met hoge winstkansen
- **Budget**: Probeer het hele budget te benutten, hoe hoger de prijs van een speler hoe meer kans op punten

## Wedstrijdschema met winstkansen
Date/Time        Home Team       Away Team        Home%  Draw%  Away%
---------------- --------------- ---------------- ------ ------ ------
Sat 27 14:30     Ajax            NAC Breda        74.8  % 15.3  % 9.9   %
Sat 27 16:45     FC Volendam     PEC Zwolle       34.9  % 26.1  % 38.9  %
Sat 27 18:00     Excelsior       PSV              10.0  % 14.5  % 75.5  %
Sat 27 19:00     Heracles Almelo Sparta Rotterdam 33.8  % 25.9  % 40.3  %
Sun 28 10:15     NEC             AZ               30.7  % 23.9  % 45.4  %
Sun 28 12:30     FC Utrecht      SC Heerenveen    52.8  % 23.6  % 23.6  %
Sun 28 12:30     FC Groningen    Feyenoord        21.4  % 23.7  % 54.8  %
Sun 28 14:45     Telstar         Go Ahead Eagles  32.3  % 26.0  % 41.8  %

## Gewenste Output Structuur

### 1. Gekozen Formatie
- Specificeer de formatie (bijv. 4-3-3)
- Motivatie voor deze keuze

### 2. Elftal Opstelling
Voor elke speler vermeld:
- **Positie**
- **Naam**
- **Club**
- **Prijs** (in miljoenen €)
- **Verwachte punten** (indien beschikbaar)
- **Aanvoerder** (markeer met (C))

### 3. Budget Overzicht
- Totale kosten van het elftal
- Restbudget (moet €0 of positief zijn)

### 4. Strategische Overwegingen
- Waarom deze spelers zijn gekozen
- Risico-analyse van het elftal
- Alternative opties indien hoofdkeuzes niet beschikbaar zijn

### 5. Club Verdeling Check
- Overzicht van hoeveel spelers per club zijn gekozen
- Verificatie dat geen club meer dan 2 spelers heeft

## Voorbeeld Output Format:

```
FORMATIE: 4-3-3

ELFTAL:
Keeper: [Naam] - [Club] - €[prijs]M
Verdediging: 
- [Naam] - [Club] - €[prijs]M
- [Naam] - [Club] - €[prijs]M  
- [Naam] - [Club] - €[prijs]M
- [Naam] - [Club] - €[prijs]M
Middenveld:
- [Naam] - [Club] - €[prijs]M
- [Naam] (C) - [Club] - €[prijs]M [AANVOERDER]
- [Naam] - [Club] - €[prijs]M
Aanval:
- [Naam] - [Club] - €[prijs]M
- [Naam] - [Club] - €[prijs]M
- [Naam] - [Club] - €[prijs]M

TOTALE KOSTEN: €[totaal]M
RESTBUDGET: €[rest]M

STRATEGISCHE MOTIVATIE:
[Uitleg van keuzes en strategie]
```

## Belangrijke Opmerkingen
- Controleer altijd dubbel of alle regels worden nageleefd
- Bij gelijke budgetruimte: kies voor de speler met hoger puntenpotentieel
- De aanvoerderskeuze is cruciaal vanwege de dubbele punten - kies verstandig!

Analyseer de beschikbare spelersdata grondig en stel het meest competitieve elftal samen binnen de gegeven beperkingen.
