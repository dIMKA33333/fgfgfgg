import random

secret_num = random.randint(1, 100)
guesses = set()
print("Угодайте число от 1 до 100")
while True:
    guess = int(input("Введите число:"))
    guesses.add(guess)
    if guess < secret_num:
        print("Больше")
        print("Ещё догадки ?")
    if guess > secret_num:
        print("Меньше")
        print("Ещё догадки ?")
    else:
        print("Поздравляем! число угаданно!")
        break
    with open('random.txt', 'w', encoding='utf-8') as f:
        for num in guesses:
            f.write(f'{num}\n')

