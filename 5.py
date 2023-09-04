import re
import os
import concurrent.futures


def task1():
    """
    Функция при помощи os.walk() рекурсивно проходит по всем папкам и файлам в path и при помощи регулярного выражения
    ищет совпадения в названии файлов. Выводит их количество. Предполагается, что ищутся файлы полностью
    совпадающие с именем filenames.txt
    """
    path = "test"
    # filename_pattern = r'\bfilename.*\.txt'
    filename_pattern = r'\bfilenames\.txt\b'

    count = 0

    file_regex = re.compile(filename_pattern)

    for root, dirs, files in os.walk(path):
        for file in files:
            if file_regex.match(file):
                count += 1

    print('Количество файлов filenames:', count)


def task2():
    """
    Функция при помощи os.walk() рекурсивно проходит по всем папкам и файлам, после чего открывает все файлы и
     при помощи регулярного выражения ищет совпадения. Далее выводит общее количество email и количество уникальных
    """
    path = "test"
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    email_addresses = list()

    for root, dirs, files in os.walk(path):
        for filename in files:
            with open(os.path.join(root, filename), 'r') as file:
                content = file.read()
                matches = re.findall(email_pattern, content)
                email_addresses.extend(matches)

    unique_email_addresses = set(email_addresses)

    print(f"Найдено {len(email_addresses)} email адрессов:")
    print(f"Из них уникальных: {len(unique_email_addresses)}")
    for email in unique_email_addresses:
        print(f'\t{email}')


def task2_optimized():
    """
    Оптимизированная функция task2. Для оптимизации используется модуль concurrent.futures, который позволяет
    выполнять задачи параллельно в нескольких потоках.
    """
    path = "test"
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    email_addresses = list()

    def find_emails_in_file(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            matches = re.findall(email_pattern, content)
            email_addresses.extend(matches)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        file_paths = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                file_paths.append(os.path.join(root, filename))

        executor.map(find_emails_in_file, file_paths)

    unique_email_addresses = set(email_addresses)

    print(f"Найдено {len(email_addresses)} email адрессов:")
    print(f"Из них уникальных: {len(unique_email_addresses)}")
    for email in unique_email_addresses:
        print(f'\t{email}')


def main():
    task1()
    task2()
    task2_optimized()


if __name__ == '__main__':
    main()
