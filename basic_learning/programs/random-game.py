import random

def create_list_game():

    while True:
        try:
            games_count = int(input('Please enter number of games you want to play: '))
            if games_count not in range(1, 6):
                print("Sorry but value must be in range from 1 to 5\n")
                continue
            else:
                if games_count == 1:
                    print(f'\nGood choice! You want to play {games_count} game')
                else:
                    print(f'\nGood choice! You want to play {games_count} games')
                break

        except ValueError as error:
            print('Wrong value')


    games_list = []
    for game_count  in range(1, games_count + 1):
        while True:
            game = str(input('Enter your {} game: '.format(game_count)))
            if not game or game.startswith(" "):
                print('Game\'s name should not be empty')
                continue
            break
        games_list.append(game)

    print('\nGreat! Here is your list of games:' )

    for games in games_list:
        print("{} game is: {}".format(games_list.index(games) + 1, games))

    return games_list


def random_method(games_list):

    print('\nDo you want to get random game? ')
    while True:
        answer = input().lower()
        if answer == 'yes':
            while True:
                random_method_list = ('Simple', 'Super')
                print('Woohoo! Now please choose my random method: 0 - {}, 1 - {}'.format(random_method_list[0], random_method_list[1]))
                method_type = int(input())
                if method_type == 0:
                    random_game = random.choice(games_list)
                    print('Easy! Your random game is: ',random_game,'enjoy your gaming!')
                    break


                elif method_type == 1:

                    games_dict = dict()
                    win_number = int(input('Yeah! This is super method! Please enter win number for game: '))

                    while True:
                        random_game = random.choice(games_list)
                        if random_game in games_dict:
                            games_dict[random_game] += 1
                        else:
                            games_dict[random_game] = 1
                        print('Game {} has {} points'.format(random_game, games_dict[random_game]))
                        if games_dict[random_game] == win_number:
                            print('\nWe did very well and finally we got the winner -', random_game)
                            print('It was awesome experience! Enjoy your gaming!')
                            break
                        else:
                            continue

                    break
                else:
                    print('Sorry, method is not found, please type 0 or 1')
            break

        elif answer == 'no':
            print("Unfortunately...but you can try again;)")
            break

        else:
            print('Please type yes or no')


print('Hello and welcome to my random program')
count = 0

while True:
    if count == 0:
        games_list = create_list_game()
        random_method(games_list)
        count += 1
    else:
        print('\nDo you want to repeat?')
        answer = input()
        if answer == "yes":
            print('Do you want to reset your games list')
            answer = input()
            if answer == "yes":
                games_list = create_list_game()
                random_method(games_list)
            else:
                random_method(games_list)
        elif answer == "no":
            print('See you later! Thank you for coming!')
            break
        else:
            print('Please type yes or no')