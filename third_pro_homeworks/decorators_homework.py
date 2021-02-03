from datetime import date, datetime
from functools import wraps


def function_logger(function):
    @wraps(function)
    def inner_function(*args, **kwargs):
        with open("C:\\Users\\озод\\PycharmProjects\\saved_works\\third_pro_homeworks\\text.log", "a+", encoding="utf-8") as log_file:
            start_time = datetime.now()
            log_file.write(
                f"Имя функции:{function.__name__} \n дата вызова: {date.today()} \n время вызова функции: {datetime.now().time()} \n")
            log_file.write(f"Аргумент *args: {args} \n Аргументы **kwargs: {kwargs} \n")
            last_function = function(*args, **kwargs)
            log_file.write(f"Результат вызова функции {function.__name__}: \n {last_function} \n")
            end_function = datetime.now() - start_time
            log_file.write(f"Всего потрачено времени: {end_function} \n")
            log_file.write(f"Документатция: {function.__doc__} \n \n")
        return last_function

    return inner_function


def with_path(file_path):
    def function_path(function):
        @wraps(function)
        def inner(*args, **kwargs):
            with open(file_path, "a+", encoding="utf-8") as log_file:
                start_time = datetime.now()
                log_file.write(
                    f"Имя функции:{function.__name__} \n дата вызова: {date.today()} \n время вызова функции: {datetime.now().time()} \n")
                log_file.write(f"Аргумент *args: {args} \n Аргументы **kwargs: {kwargs} \n")
                last_function = function(*args, **kwargs)
                log_file.write(f"Результат вызова функции {function.__name__}: \n {last_function} \n")
                end_function = datetime.now() - start_time
                log_file.write(f"Всего потрачено времени: {end_function} \n")
                log_file.write(f"Документатция: {function.__doc__} \n \n")
            return last_function

        return inner

    return function_path



