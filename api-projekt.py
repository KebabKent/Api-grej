import requests
import webbrowser
import time


def time_reveal():
    print('In')
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)


class Spel:
    def roll_dice():
        dice_req = requests.get('http://roll.diceapi.com/json/d6')
        dice = dice_req.json()
        return dice['dice'][0]['value']

    def fox_pic():
        fox_req = requests.get('http://randomfox.ca/floof')
        fox = fox_req.json()
        webbrowser.open(fox['image'])

    def chuck_joke():
        chuck_req = requests.get('https://api.chucknorris.io/jokes/random')
        chuck = chuck_req.json()
        print('\n' + chuck['value'] + '\n')


spelare = Spel


def fifty_fifty_spel(spelare):
    while True:
        ans = int(input('Game Menu\nPlay (1)\nGame rules (2)' +
                        '\nquit (3)\n\nAnswer: '))

        if ans == 1:
            print('')
            dice_val = spelare.roll_dice()
            print(f'Dice value: {dice_val}')

            if dice_val > 3:
                print('Chuck Norris joke!\n')
                time_reveal()
                spelare.chuck_joke()

            elif dice_val <= 3:
                print('Fox picture')
                time_reveal()
                spelare.fox_pic() 

        elif ans == 2:
            print('\nApi rolls dice. \nValue determines outcome.\n' + 
                            'If value over three chuck Norris joke.\n' +
                            'if under or equal to three fox picture.\n')

        elif ans == 3:
            print('\nGoodbye!')
            break

        else:
            print('Answer is invallid please try again!')


fifty_fifty_spel(spelare)

