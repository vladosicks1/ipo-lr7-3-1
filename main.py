import json 


with open("fish.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) 

count = 0 
num = 0

for fish in data:
    num+=1

num+=1

while True:
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)

    number = int(input("Введите номер действия: "))

    if number == 1:
        for fish in data:
            print(f"""
            Номер записи: {fish['id']}, 
            Общее название: {fish['name']},                       
            Латинское название: {fish['latin_name']}, 
            Пресноводная: {fish['is_salt_water_fish']},    
            Кол-во подвидов: {fish['sub_type_count']} 
            """)
        count += 1

    elif number == 2:
        id = int(input("Введите номер рыбы: "))
        find = False    
        for fish in data:
            if id == fish['id']:
                print(f"""
                Номер записи: {fish['id']}, 
                Общее название: {fish['name']},                       
                Латинское название: {fish['latin_name']}, 
                Пресноводная: {fish['is_salt_water_fish']},    
                Кол-во подвидов: {fish['sub_type_count']} 
                """)
                find = True  
                break  
        count += 1
        if not find:
            print("Запись не найдена.")
 
    elif number == 3:
        flag = True
        name = input("Введите название: ")  
        latin_name = input("Введите латинское название: ")  
        is_salt_water_fish = input("Введите, пресноводная ли рыба (да/нет): ")  
        sub_type_count = input("Введите кол-во подвидов: ")
        try:
            sub_type_count = int(sub_type_count)
        except:
            flag = False
        if(not flag):
            print("Значение введено неверно.")
            break
        else:
            new_fish = {
                'id': num,
                'name': name,
                'latin_name': latin_name,
                'is_salt_water_fish': True if is_salt_water_fish.lower() == 'да' else False, 
                'sub_type_count': sub_type_count
            }

            data.append(new_fish) 
            with open("fish.json", 'w', encoding='utf-8') as out_file: 
                json.dump(data, out_file)
            print("Рыба успешно добавлена.")
        count += 1
        num+=1

    elif number == 4:
        id = int(input("Введите номер рыбы: "))
        find = False  

        for fish in data:
            if id == fish['id']:
                data.remove(fish)  
                find = True  
                break 

        if not find:
            print("Запись не найдена.")
        else:
            with open("fish.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Запись успешно удалена.")
        count += 1

    elif number == 5:
        print(f"""Программа завершена.
               Кол-во операций: {count}""")
        break


    else:
        print("Такого номера нет.")