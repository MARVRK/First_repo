

# Сутності:

# Field: Базовий клас для полів запису.                                                           +
# Name: Клас для зберігання імені контакту. Обов'язкове поле.                                     +
# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).                    +
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.         +
# AddressBook: Клас для зберігання та управління записами.


# Функціональність:

# AddressBook:Додавання записів.  +
# Пошук записів за іменем.        +
# Видалення записів за іменем.    +

# Record:Додавання телефонів.     +
# Видалення телефонів.            +
# Редагування телефонів.          +
# Пошук телефону.                 +



##############################################################
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def new_contact(self, name: str)->None:
        if name is None:                   # Check if name is not empty
           raise ValueError ("Record must contain name!")
        self._name=name
              
class Phone(Field):
    def add_phone(self, cell_number: int)->None:
        cell_number = str(cell_number)    # Convert to string for length check
        if len(cell_number) != 10:
            raise ValueError("Phone number must contain 10 digits!")
        self.number = cell_number

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.name.new_contact(name)        # Call contact name to check if it's not none.
        self.phones = []

   
    def add_phone(self, phone_number: int):
        phone_field = Phone(phone_number)
        phone_field.add_phone(phone_number) # Call number_validate method to validate the phone number (not les then 10 digits)
        self.phones.append(phone_field)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.number == phone_number:
                self.phones.remove(phone)
    
    def edit_phone(self, old_phone_number: str, new_phone_number: str):
        for phone in self.phones:
            if phone.number == old_phone_number:
                self.phones.remove(phone)
                new_phone=Phone(new_phone_number)
                new_phone.add_phone(new_phone_number)
                self.phones.append(new_phone)
            
    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.number == phone_number:
                return phone 
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, name, record):
       self.data[name] = record

    def find(self,name):
        return self.data[name]

    def delete(self,name):
        del self.data[name]

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
book.add_record("John", john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record("Jane",jane_record)

# # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john_record.edit_phone("1234567890","1112223333")
john_record.find_phone("1112223333")

print(john_record)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")