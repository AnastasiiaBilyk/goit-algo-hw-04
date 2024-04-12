path = 'C:\Projects\My_repo\goit-algo-hw-04\cats_file.txt'
def get_cats_info(path):
    cats_list = []
    try:
        with open (path, 'r', encoding='UTF-8') as file: 
            for line in file:
                cats_info_list = id, name, age = line.strip().split(',')
                cats_list.append(dict({"id": id, 'name': name, 'age': age}))
            return cats_list     
    except FileNotFoundError: 
        print('Файл не знайдено')

result = get_cats_info(path)
print(result)
