"""Пользователь вводит с клавиатуры два числа (начало
в этом диапазоне. Вывод на экран должен проходить по
правилам, указанным ниже.
Если число кратно 3 (делится на 3 без остатка) нужно
вывести слово Fizz. Если число кратно 5 нужно выве1
сти слово Buzz. Если число кратно 3 и 5 нужно вывести
Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
само число."""

while True:
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        if start > end:
            raise ValueError
        for number in range(start, end + 1):
            if number % 3 == 0 and number % 5 == 0:
                print("Fizz Buzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)
        break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите начало и конец диапазона.")
