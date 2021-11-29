import time


def perf_time(func):
    def wrapper(*args, **kwargs):
        print(f"Была вызвана функция {func.__name__}")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции: {end - start} секунд")
    return wrapper


@perf_time
def my_lovely_function():
    some_list = []
    for _ in range(100000):
        some_list.append(1)


@perf_time
def some_another_function(n):
    for _ in range(n):
        pass


if __name__ == '__main__':
    my_lovely_function()
    some_another_function(10000000)

