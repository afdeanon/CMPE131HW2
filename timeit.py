import time
def calculate_time(func):
    def wrapper():
        initial = time.time()
        function = func()
        final = time.time()
        print("Total time " + str(final - initial))
        #return function
    return wrapper
