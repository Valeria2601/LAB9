import random
import logging
# Настройка логгера
logging.basicConfig(filename='logfile.log', level=logging.INFO)

def generate_sequence(n):
    "Генерирует список чисел от 1 до n в случайном порядке"
    sequence = list(range(1, n+1))
    random.shuffle(sequence)  # перемешиваем список
    return sequence

def display_sequence(sequence):
    "Вывод на экран последовательность чисел"
    print("Последовательность чисел:")
    for number in sequence:
        print(number)

def play_game():
    while True:
        try:
            n = int(input("Введите число количество бочонков: "))
            if n < 1:
                raise ValueError("Число должно быть больше 0")
            break
        except ValueError:
            print("Неправильный ввод, попробуйте снова")

    sequence = generate_sequence(n)
    display_sequence(sequence)

    for number in sequence:
        input("Нажмите Enter, чтобы вытянуть очередной бочонок")
        print(f"Вытянутый бочонок: {number}")
        logging.info(f"Вытянутый бочонок: {number}")

play_game()