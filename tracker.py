def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
    wrapper.counter = 0
    return wrapperdef func_counter):
	counter = 0
