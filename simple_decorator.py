import logging

logging.basicConfig(
    filename="function_calls.log",
    format="%(levelname)s %(name)s %(asctime)s %(message)s",
    level=logging.INFO,
)


def log_calls(func):
    def _wrapper(*args, **kwargs):
        logging.info(func.__name__)
        return_value = func(*args, **kwargs) # calls spam() (or other passed-in function)
        return return_value
    return _wrapper

@log_calls
def spam(repeat):
    print("spam" * repeat)
# spam = deco(spam)  # replace spam with _wrapper

@log_calls
def ham():
    print("hammmmmmmm")

spam(2) # calls spam(), etc
ham()
ham()
spam(5)
spam(1)
ham()