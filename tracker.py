def func_counter(func):
    def wrapper(*args):
        wrapper.counter += 1
    wrapper.counter = 0
    return wrapper
