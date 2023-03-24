import time

from fibo import fibo


def main():
    """Печать 1000 элемента последовательности Фибоначчи"""
    tic = time.perf_counter()
    result = fibo(1000)
    toc = time.perf_counter()
    print(f"Вычисление заняло {toc - tic:0.4f} секунд")
    print(result)


if __name__ == "__main__":
    main()