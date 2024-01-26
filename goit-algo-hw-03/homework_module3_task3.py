import re

def normalize_phone(phone_number):
    pattern=r"[\d\+]"
    formatted_numbers="".join(re.findall(pattern,phone_number))
    if len(formatted_numbers)==10:
        formatted_numbers="+38"+ formatted_numbers
    elif len(formatted_numbers)==12:
        formatted_numbers="+"+formatted_numbers
    return formatted_numbers

raw_numbers=["    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]

for num in raw_numbers:
    print (normalize_phone(num))
