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
Därefter kommer metoden roll_dice() kallas från klassen. Den returnerar ett tärnings värde 
mellan 1 och 6. Om värdet är 3 eller mindre kommer klassen att hämta in en random URL-länk
från API:en http://randomfox.ca med bilden på en räv och öppna den i webbläsaren med hjälp av python 
biblioteket webbrowser. Om värdet är över tre kommer ett Chuck Norris skämt att printas. Innan någon 
av prosesserna sker kommer programmet att räkna ner från fem för dramatisk effekt innan bilden eller
skämtet visas i antingen terminalen eller webbläsaren. 


## UML-Diagram
![Skärmbild (3)](https://user-images.githubusercontent.com/91462301/153832079-8b6748ef-095a-4059-b765-bca62061a98a.png)


## Installation
Det ända som behöver installeras för att köra programmet är Python biblioteket requests.

```powershell
pip install requests
```


## Medvetna fel (issue tracker)
Inga medvetna fel förekommer.


## To do
Det finns ingen anledning att fortsätta utveckla programmet. Det är väldigt simpelt och har bara ett 
examinerande värde.


## Att bidra (contribution)
Inga bidrag kommer accepteras.
Det är ett skolprojekt och behöver inte vidare utvecklas.
Det går bra att använda koden för eget bruk men jag ser ingen riktig anledning för att göra det.
Om du använder programmet får du gärna ange mig som en Contributor men det gör inget om inte.


## Licens (License)
[MIT](https://choosealicense.com/licenses/mit/)


## Kontakt information
Noneofyourdamnbuissnes.com
