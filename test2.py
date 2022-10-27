# # import multiprocessing
# # import time
# #
# #
# # def heavy(n, i, proc):
# #     for x in range(1, n):
# #         for y in range(1, n):
# #             x ** y
# #     print(f"Цикл № {i} ядро {proc}")
# #
# #
# # def sequential(calc, proc):
# #     print(f"Запускаем поток № {proc}")
# #     for i in range(calc):
# #         heavy(500, i, proc)
# #     print(f"{calc} циклов вычислений закончены. Процессор № {proc}")
# #
# #
# # def processesed(procs, calc):
# #     # procs - количество ядер
# #     # calc - количество операций на ядро
# #
# #     processes = []
# #
# #     # делим вычисления на количество ядер
# #     for proc in range(procs):
# #         p = multiprocessing.Process(target=sequential, args=(calc, proc))
# #         processes.append(p)
# #         p.start()
# #
# #     # Ждем, пока все ядра
# #     # завершат свою работу.
# #     for p in processes:
# #         p.join()
# #
# #
# # if __name__ == "__main__":
# #     start = time.time()
# #     # узнаем количество ядер у процессора
# #     n_proc = multiprocessing.cpu_count()
# #     # вычисляем сколько циклов вычислений будет приходится
# #     # на 1 ядро, что бы в сумме получилось 80 или чуть больше
# #     calc = 80 // n_proc + 1
# #     processesed(n_proc, calc)
# #     end = time.time()
# #     print(f"Всего {n_proc} ядер в процессоре")
# #     print(f"На каждом ядре произведено {calc} циклов вычислений")
# #     print(f"Итого {n_proc * calc} циклов за: ", end - start)
#
# import multiprocessing as mp
# import time
# from itertools import permutations
#
# w = (["V", 5], ["X", 2], ["Y", 1], ["Z", 3])
# chars = """~,!@"'#$%^&*()[]{}-<>/\.:;=+?abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"""
# # length = int(input('длина пароля?' + "\n"))
# length = 3
# data = permutations(chars, length)
# # print(data)
#
# def work_log(_data):
#     start = time.time()
#     counter = 0
#     for comb in range(100000):
#         counter += 1
#     print(f"Поток какой-то там, counter = {counter}")
#     print(f"Итоговое время потока: {time.time() - start}")
#
#     pass
#
#
# def handler():
#     p = mp.Pool(mp.cpu_count())
#     p.map(work_log, data)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     handler()
#     print(f"Всего {mp.cpu_count()} ядер в процессоре")
#     print(f"Итоговое время: {time.time() - start}")


import string
import multiprocessing as mp
import itertools
import os
from random import choice
import time


# def do_job(first_letter):
#     counter = 0
#     for x in itertools.combinations_with_replacement(alphabet, alphabet, alphabet):
#         newb = tuple(first_letter) + x
#         # print(newb)
#         # if newb == (('#', ',') or ('~', '{') or ('^', '~') or ('~', '~')):
#         if isinstance(newb, tuple):
#             print(f"Gotcha!")
#             break
#         counter += 1
#         # print(x)
#     print(f"{counter}")


def job(password, first_letter, chars, length, flag, verboseflag):
    counter = 0
    for x in itertools.permutations(chars, length):
        newb = tuple(first_letter) + x
        if (verboseflag):
            # print(newb)
            print(f"{os.getpid()} of {os.getppid()} is trying {newb}\n")
        # if newb == (('#', ',') or ('!', '!') or ('~', '~') or ('!', '~')):
        if ("".join(newb)) == password:
            # if isinstance(newb, tuple):
            print(f"Gotcha!")
            flag.value = 1
            break
        counter += 1
        if (flag.value == 1):
            break
        # print(x)
    print(f"{counter}")
    pass


# if __name__ == "__main__":
#     pool = mp.Pool()
#     results = []
#     for i in range(num_parts):
#         if i == num_parts - 1:
#             first_bit = alphabet[part_size * i:]
#         else:
#             first_bit = alphabet[part_size * i: part_size * (i + 1)]
#         results.append(pool.apply_async(do_job(first_bit)))
#
#     pool.close()
#     pool.join()
#
# if __name__ == "__main__":
#     pool = mp.Pool()
#     results = []
#     for i in alphabet:
#         res = pool.apply_async(do_job(i))
#         if (res):
#             results.append(res)
#
#     pool.close()
#     pool.join()
#     print(results)

def main():
    alphabet = """~,!@"'#$%^&*()[]{}-<>/\.:;=+?abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"""
    # num_parts = 4
    # part_size = len(alphabet) // num_parts
    processes = []
    flag = mp.Value('i', 0)
    verbose = True
    length = int(input('длина пароля?' + "\n"))
    password = ''
    for i in range(length):
        password += choice(alphabet)
    print("Ваш пароль: ", password)
    start_time = time.time()
    for l in alphabet:
        processes.append(mp.Process(target=job, args=(password, l, alphabet, length - 1, flag, verbose)))
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()
    print("--- %s seconds (Hacking) ---" % (time.time() - start_time))
    pass


if __name__ == "__main__":
    main()
