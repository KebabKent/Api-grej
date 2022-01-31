import requests
import webbrowser
import time


def time_reveal():
    print('IN')

    for i in range(5,0,-1):
        print(i)
        time.sleep(1)


class Spel:
    def __init__(self, fox, dice, chuck):
        self.fox = fox
        self.dice = dice
        self.chuck = chuck

    def __str__():
        pass

    def roll_dice():
        y = requests.get('http://roll.diceapi.com/json/d6')
        dice = y.json()
        return dice['dice'][0]['value']

    def fox_pic():
        x = requests.get('http://randomfox.ca/floof')
        fox = x.json()
        webbrowser.open(fox['image'])

    def chuck_joke():
        z = requests.get('https://api.chucknorris.io/jokes/random')
        chuck = z.json()
        print('\n' + chuck['value'] + '\n')


fettma = Spel


def fifty_fifty_spel(fettma):
    while True:
        ans = int(input('Game Menu\nPlay (1)\nGame rules (2)' +
                        '\nquit (3)\n\nAnswer: '))

        if ans == 1:
            print('')
            dice_val = fettma.roll_dice()
            print(f'Dice value: {dice_val}')

            if dice_val > 3:
                print('Chuck Norris joke!\n')
                time_reveal()
                fettma.chuck_joke()

            elif dice_val <= 3:
                print('Fox picture')
                time_reveal()
                fettma.fox_pic()
        


        # elif annat gamemode. 

        # elif ännu ett gamemode. 



        elif ans == 2:
            print('\nApi rolls dice. \nValue determines outcome.\n' + 
                            'If value over three chuck Norris joke.\n' + 
                            'if under or equal to three fox picture.\n')

        elif ans == 3:
            print('\nGoodbye!')
            break

        else:
            print('Answer is invallid please try again!')


fifty_fifty_spel(fettma)


"""

Utöka spelet. Gör mer saker typ gamemodes och liknande.

"""