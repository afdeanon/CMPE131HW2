def fun_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
    wrapper.counter = 0
    return wrapper
