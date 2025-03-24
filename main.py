# Определение функции
def sum_negative_between_min_max(array):
    min_index = array.index(min(array)) # Индекс минимального элемента
    max_index = array.index(max(array)) # Индекс максимального элемента
    start, end = sorted([min_index, max_index]) # Определение начала и конца диапазона
    negative_sum = 0 # Инициализация переменной для суммы отрицательных элементов
    for i in array[start + 1:end]: # Перебор каждого элемента
        if i < 0: # Если элемент отрицательный, добавляем к сумме
            negative_sum += i
    return negative_sum # Возвращаем итоговую сумму

# Основной блок выполнения программы
if __name__ == "__main__":
    try:
        # Запрашиваем ввод элементов массива и преобразование в список целых чисел
        input_array = list(map(int, input("Введите элементы массива через пробел: ").split()))
        # Проверка, что в массиве есть как минимум два элемента
        if len(input_array) < 2:
            print("Ошибка: массив должен содержать не менее двух элементов")
            input()
        else:
            # Вызов функции и вывод суммы отрицательных элементов
            result = sum_negative_between_min_max(input_array)
            print(f"Сумма отрицательных элементов: {result}")  
            input() 
    except ValueError: # Обработка ошибки, если введены нечисловые данные
        print("Ошибка: все элементы должны быть целыми числами")
        input()
