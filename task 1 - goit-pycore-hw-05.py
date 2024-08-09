# Вимоги до завдання:
# Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
# fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
# Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.


def caching_fibonacci() -> callable:
    cache = {}  # словник для зберігання результатів обчислень

    def fibonacci(n: int) -> int:
        # If n <= 0 --> 0
        if n <= 0:
            return 0
        # If n == 1 --> 1
        elif n == 1:
            return 1
        # If n exists --> return n
        elif n in cache:
            return cache[n]
        # If n does not exist --> calculate 
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610