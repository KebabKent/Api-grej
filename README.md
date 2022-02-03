# API projekt - 50/50 Chuck/Fox

## Teknologier/Språk

Hela projektet är skrivet i Python. Mer specifikt är det Python 3.9.1. 
Programmet använder sig av de inbyggda Python biblioteken webbrowser och time.
Det änvänder sig även av biblioteket requests.

## Hur det fungerar (Usage)

Programmet börjar med att skapa en spelare i Spel klassen. Efter det startar 
den funktionen "fifty_fifty_spel()" som kör en while loop som fungerar som själva spelet. 
I while loopen frågar den vad spelaren vill göra:
- Play (1)
- Game rules (2)
- quit (3)
Om spelaren väljer 3 stängs spelet ner. Om spelaren väljer två kommer spelreglerna skrivas upp
och sedan komma tillbaka till spelmenyn. Om spelaren väljer 1 kommer spelet att köras.
Därefter kommer metoden roll_dice() kallas från klassen. Den returnerar ett tärnings värde. 
Alltså ett nummer mellat 1 och 6. 













## Licens (License)

[MIT](https://choosealicense.com/licenses/mit/)

