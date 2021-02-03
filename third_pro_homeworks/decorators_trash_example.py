from functools import wraps


# def decorate_1(function):
#     def decorate_2(*args, **kwargs):
#         print("first person hello!")
#         function(*args, **kwargs)
#         print("third person hello!")
#     return decorate_2
#
#
# def say(name, surname):
#     print(f"second person {name} {surname} hello!")
#
# b = decorate_1(say)
# b("ozod", "ochilboyev")


def decorator(function):
    @wraps(function)
    def first_step(*args, **kwargs):
        print("first logic")
        print("start your function:")
        result = function(*args, **kwargs)
        print(result)
        print("end your function")
        print("end function")
        return result

    return first_step


@decorator
def say(*args,  **kwargs):
    return f'{args} - {kwargs}'


say("hello", "world")
