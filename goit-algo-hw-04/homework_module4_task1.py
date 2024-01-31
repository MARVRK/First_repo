from pathlib import Path

def total_salary(path):
    overall_salary=0
    average_salary=0
    extracted_data=[]
    try:   
        if source.stat().st_size>1:                                                                  # if size less then initially - False
            with open(path, 'r',encoding='utf-8') as fh:
                for line in fh.readlines():
                    numbers=[int(num) for num in line.split(',') if num.strip().isdigit()]           # here we split the string on separete lists and want to extract only the digits.
                    extracted_data.extend(numbers)                                                                                             
                    overall_salary+=sum(numbers)
                    if extracted_data==[0]:
                        print("cannot divide average salary on 0")
                    else:
                        average_salary=overall_salary/len(extracted_data)
            return overall_salary,average_salary
        else:
            print("file is empty")   
    except FileNotFoundError :
        print("Cannot find file:'salary_data.txt'")

# with open('salary_data.txt', 'w') as fh:
#        fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')

source=Path('salary_data.txt')
import_salary_data=total_salary(source) 
if import_salary_data :
    overall,average = import_salary_data
    print(f"Загальна сума заробітної плати: {overall}, Середня заробітна плата: {average}")

