# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, 
# що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. 
# Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

import re
from typing import Callable


def generator_numbers(text: str):

    # Use of a regular expression to find all the numbers in the text

    pattern = r"\b\d+\.\d+\b"  # Numbers look like one or more digits, a period, and one or more digits
    
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Return of a number as a result


def sum_profit(text: str, func: Callable):
    total = sum(
        func(text)
    )  
    
    # Recall of generator_numbers and sum of all the numbers returned by the generator

    return total


# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# Очікуване виведення: Загальний дохід: 1351.46
