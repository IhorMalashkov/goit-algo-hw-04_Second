from pathlib import Path

file_name = Path('.')

def get_cats_info(path):
    cats = []
    try:             
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    id, name, age = line.split(',')
                    cats.append({"ID": id, "Name": name, "Age": age})
                if not line:
                    continue
        return cats
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
    except ValueError:
        print("Помилка: Файл містить некоректні дані.")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")

cats_info = get_cats_info("path/to/cats_file.txt")
print(*cats_info, sep='\n')