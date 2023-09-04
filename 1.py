import os


def black_book(page: int) -> bool:
    status_code = os.system(f"./black-book -n {page}")
    return status_code == 0


def find_last_page():
    """
    Так как страницы в книге отсортированы по возрастанию, то можно использовать алгоритм бинарного поиска.
    Для определения есть ли страница в книге используется функция black_book.

    Уточнение к уточнению:
        я предполагаю, что в уточнении опечатка, ведь там сказано, что функция black_book возвращает True, если
        введённый номер страницы является последним, что некорректно в данном случае т.к. функция возвращает True,
        если страница просто есть в книге.
    """
    left, right = 1, 10000000
    last_page = 0

    while left <= right:
        middle = (left + right) // 2
        check_black_book = black_book(middle)

        if check_black_book:
            last_page = middle
            left = middle + 1
        else:
            right = middle - 1

    return last_page


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_book) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        black_book возвращает True, если страница последняя
                  возвращает False, если страница не последняя.
    
    
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """

    last_page = find_last_page()
    print("Номер последней страницы:", last_page)


if __name__ == '__main__':
    main()