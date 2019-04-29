import random


games_qty = 0

while games_qty <= 0:
    print(f'How many games would you like to play?')
    games_qty = int(input())

for x in range(games_qty):
    current_guess = 0
    number = random.randint(1, 25)
    guesses_count = 1

    while current_guess != number:
        print(f'\nGame number: {x+1}')
        print(f'Choose a number between 1 and 25')
        current_guess = int(input())
        if current_guess > number:
            print(f'Your guess is higher than my number')
        elif current_guess < number:
            print(f'Your guess is lower than my number')
        else:
            if guesses_count > 1:
                try_count = 'tries'
            else:
                try_count = 'try'
            print(f'You guessed my number with only {guesses_count} {try_count}. Congratulations!')
        guesses_count += 1

print(f'Game Over!')
