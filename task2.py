import random
with open('questions.txt', 'r', encoding='utf-8')as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line)
with open('response.txt', 'r', encoding='utf-8') as file:
    liness = file.readlines()
    random_lines = random.choice(liness)
    print(random_lines)