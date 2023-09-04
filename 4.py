import sys
import json


def get_all_questions(data):
    """
    Вспомогательная функция, которая получает список всех вопросов из json файла
    """
    all_questions = list()

    for elem in data:
        questions = elem.get("questions")
        if questions:
            all_questions.extend(questions)

    return all_questions


def count_questions(data: dict):
    """
    Считает общее количество вопросов
    """
    questions_count = len(get_all_questions(data["game"]["rounds"]))

    print(f"Общее количество вопросов: {questions_count}")


def print_right_answers(data: dict):
    """
    Выводит все правильные ответы
    """
    all_questions = get_all_questions(data["game"]["rounds"])
    all_correct_answer = list()

    for question in all_questions:
        correct_answer = question.get("correct_answer")
        if correct_answer:
            if isinstance(correct_answer, list):
                all_correct_answer.extend(correct_answer)
            else:
                all_correct_answer.append(correct_answer)


    print("Правильные ответы:")
    for answer in all_correct_answer:
        print(f'\t{answer}')


def print_max_answer_time(data: dict):
    """
    Выводит максимальной время ответа на вопрос
    """
    max_answer_time = 0
    all_questions = get_all_questions(data["game"]["rounds"])
    for question in all_questions:
        time_to_answer = question.get("time_to_answer", 0)
        max_answer_time = max(max_answer_time, time_to_answer)

    print(f"Максимальное время ответа: {max_answer_time}")


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Для запуска скрипта передайте имя файла через аргумент командной строки: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
