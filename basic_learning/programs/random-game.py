import random


def create_list_game():

    while True:
        try:
            games_number = int(input('Please enter number of games you want to play: '))
            if games_number not in range(2, 6):
                print("Sorry but value must be in range from 2 to 5\n")
                continue
            else:
                print(f'\nGood choice! You want to play {games_number} games')
                break

        except ValueError as error:
            print('Wrong value')
    games = []
    for game_number in range(1, games_number + 1):
        while True:
            game = str(input('Enter your {} game: '.format(game_number))).strip()
            if not game:
                print('Game\'s name should not be empty')
                continue
            break
        games.append(game)

    print('\nGreat! Here is your list of games:')

    for game in games:
        print("{} game is: {}".format(games.index(game) + 1, game))

    return games


def random_method(games):

    print('\nDo you want to get random game? ')
    while True:
        yes_no = input().lower()
        if yes_no == 'yes':
            while True:
                random_method_list = ('Simple', 'Super')
                print('Please choose random method: 0 - {0[0]}, 1 - {0[1]}'.format(random_method_list))
                method_type = int(input())
                if method_type == 0:
                    random_game = random.choice(games)
                    print('Easy! Your random game is: ', random_game, 'enjoy your gaming!')
                    break
                elif method_type == 1:
                    games_dict = dict()
                    win_number = int(input('Yeah! This is super method! Please enter win number for game: '))
                    while True:
                        random_game = random.choice(games)
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

        elif yes_no == 'no':
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
        answer = input().lower()
        if answer == "yes":
            print('Do you want to reset your games list')
            answer = input()
            if answer == "yes":
                new_games_list = create_list_game()
                random_method(new_games_list)
            else:
                random_method(games_list)
        elif answer == "no":
            print('See you later! Thank you for coming!')
            break
        else:
            print('Please type yes or no')
