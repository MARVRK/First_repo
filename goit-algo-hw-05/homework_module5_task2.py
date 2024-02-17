from typing import Callable
import re
import math

def generator_numbers(text: str):
    pattern=r'\d{1,4}(?:.\d{2})?'
    for match in re.findall(pattern,text):
        yield match
        
def sum_profit(text: str, func: Callable):
    total=[]
    for number in func(text):
        total.append(float(number))
    return math.fsum(total)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
