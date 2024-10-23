import time
try:
    for i in range(1,4):
        with open(f'input{i}.txt','r',encoding='utf-8') as file:
          words = file.readline()
          combine = file.readline()

          start_time = time.time()  # Запуск таймера
          elapsed_time = time.time() - start_time  # Время, прошедшее с начала ввода
          if elapsed_time > 5:
              print("Время вышло! Игра окончена.")
              break

except FileNotFoundError:
    print('ww')