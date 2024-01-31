from pathlib import Path

def get_cats_info(path):
    cats_data_list=[] 
    try:
        if source.stat().st_size>0:                                                    
                with open(path, 'r',encoding='utf-8') as fh:
                    for line in fh.readlines():
                        raw_data=[part.strip() for part in line.split(',')]
                        cats_data_list.append({"id":raw_data[0],"name":raw_data[1],"age":raw_data[2]})       
                return cats_data_list
        else:
            print("file is empty")   

    except FileNotFoundError :
        print("Cannot find file:'crazy_cats.txt'")
    except IndexError:
        print("searched index is out of range")
   
# with open('crazy_cats.txt', 'w') as file:
        # file.write('60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5')

source=Path('crazy_cats.txt')
cats_info=get_cats_info(source) 
print(cats_info)


