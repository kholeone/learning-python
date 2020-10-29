def upper_decorator(func):
    def function_wrapper(string_1, string_2):
        return string_1.upper() + " " + string_2.lower()
    return function_wrapper

@upper_decorator
def hello(string_1, string_2):
    return string_1 + " " + string_2

print(hello("hello world", "HELLO WORLD"))