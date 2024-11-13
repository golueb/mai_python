def open_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for line in data:
            try:
                number = float(line[0:len(line)-1])
                print(number)
            except ValueError:
                raise Exception('TypeError')
    except FileNotFoundError:
        print('файл не найден')
    finally:
        file.close()

open_file('data.txt')