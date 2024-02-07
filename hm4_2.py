def get_cats_info(path):
    cats_info = []

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            cat_id, cat_name, cat_age = line.strip().split(',')
            cat_info = {"id": cat_id, "name": cat_name, "age": cat_age}
            cats_info.append(cat_info)
    

    return cats_info


cats_file_path = input("Введіть шлях до файлу: ")
cats_info = get_cats_info(cats_file_path)

if cats_info:
    print(cats_info)