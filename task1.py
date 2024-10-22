try:
    students_results = []
    total_average = 0
    total_students = 0
    for i in range(1,11):
        try:
            with open(f'input{i}.txt','r',encoding='utf-8') as file:
                name = file.readline().strip()
                print(name)
                grades = file.readline().strip().split()
                print(grades)
                total = sum(float(grade) for grade in grades if grade != 'нб')
                count = sum(1 for grade in grades if grade != 'нб')
                average = total // count
                students_results.append(f'{name}:{average:.2f}')
                total_average += average
                print(total_average)
                total_students += 1
            print(total_average)
            print('Всего студентов:', total_students)
            average_top = total_average / total_students
            print(f"Общая успеваемость :{average_top:.2f}")
        except ZeroDivisionError as e:
            print('Деление на 0 невозможно')
    try:
        with open('output.txt','w',encoding='utf-8') as output_file:
            output_file.write('\n'.join(students_results) + '\n')
            output_file.write(f'Общ.средняя успеваемость: {average_top:.2f}')
    except Exception as e:
        print('Запись не удалась')
except FileNotFoundError as e:
    print('Файл не найден')

