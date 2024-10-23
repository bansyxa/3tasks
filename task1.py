import random
guessed_number = random.randint(1, 100)
attemps = 0
answers = set()
print('Я загадал число от 1 до 100, попробуй угадать')
while True:
    attemps += 1
    try:
        input_number = int(input(f'Попытка {attemps}. Введите число: '))
        answers.add(input_number)
    except ValueError as e:
        print('сори бро')
        continue

    if input_number < guessed_number:
        print('Больше')
    elif input_number > guessed_number:
        print('Меньше')
    else:
        print(f'Круто!Вы угадали число {input_number} за {attemps} попыток')
        break

with open('random.txt', 'w', encoding='utf-8') as file:
    file.writelines(str(answers))