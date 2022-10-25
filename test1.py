import time
import zlib
from itertools import permutations, combinations_with_replacement
from random import choice


def shift_left(input):
    result = input << 0x10
    if result > 0xffffffffffffffff:
        result = result & 0xffffffffffffffff
    else:
        result = result

    return result


poly = 0xEDB88320

crc_table = [0] * 256
crc = 0
for i in range(256):
    crc = i
for j in range(8):
    if crc & 1:
        crc = (crc >> 1) ^ poly
else:
    crc = crc >> 1
crc_table[i] = crc


def crc32_3(string):
    crc = 0xffffffff
    for ch in string:
        crc = crc_table[(crc ^ ord(ch)) & 0xff] ^ (crc >> 8)
    return crc ^ 0xffffffff


# def crc32(bytes: list = []):
#     _crc32 = 0xFFFFFFFF
#     for byte in bytes:
#         lookupindex = (_crc32 ^ byte) and 0xFF
#         t = _crc32
#         for i in range(8):
#             t = shift_left(t)
#
#         _crc32 = t ^ CRCTable[lookupindex]  # CRCTable is an array of 256 32-bit constants
#         pass
#     # _crc32 = _crc32 ^ 0xFFFFFFFF
#     _crc32 = ~_crc32  # inverting all bytes

# crc32()
# crc32([])


def brut3(chars, inputpassword):
    # hashed = zlib.crc32(inputpassword.encode('utf-8'))
    start_time = time.time()
    wrongPasswords = set()
    length = len(inputpassword)
    while True:
        password = ''
        for i in range(length):
            password += choice(chars)

        if password not in wrongPasswords:
            # if zlib.crc32(password.encode('utf-8')) != hashed:
            if password != inputpassword:
                wrongPasswords.add(password)
            else:
                break

    print(password + " is correct")
    print("--- %s seconds (Hacking) ---" % (time.time() - start_time))


def brut5(chars, corpass):
    start_time = time.time()
    password = ''
    length = len(corpass)

    # for sym in chars:
    # for comb in generator(chars, length):
    counter = 0
    for comb in permutations(chars, length):
        # print(''.join(comb))
        if (''.join(comb) == corpass):
            password = comb
            break
        counter += 1
    print("Number of combinations:", counter)
    print(str(password) + " is correct")
    print("--- %s seconds (Hacking) ---" % (time.time() - start_time))
    pass


def brut6(chars, corpass):
    start_time = time.time()
    password = ''
    length = len(corpass)

    # for sym in chars:
    # for comb in generator(chars, length):
    counter = 0
    for comb in combinations_with_replacement(chars, length):
        # print(''.join(comb))
        counter += 1
        if (''.join(comb) == corpass or ''.join(comb) == str(corpass[::-1])):
            password = comb
            break

    print("Number of combinations:", counter)
    print(str(password) + " is correct")
    print("--- %s seconds (Hacking) ---" % (time.time() - start_time))
    pass


def brut4(_chars, _corpass):
    # hashed = zlib.crc32(_corpass.encode('utf-8'))
    start_time = time.time()
    correctPassword = _corpass
    password = ""
    length = len(_corpass)
    chars = _chars
    wrongPasswords = set()

    run = True

    while run:
        password = ''
        for i in range(length):
            password += choice(chars)

        if password not in wrongPasswords:
            if password == correctPassword:
                run = False
            else:
                wrongPasswords.add(password)

    print(password + " is correct")
    print("--- %s seconds ---" % (time.time() - start_time))


def generator(chars, passlength):
    # for combination in combinations(chars, 3):
    #     print(combination)
    start_timesp = time.time_ns()
    counter = 0
    # print(str(permutations(chars, passlength)))
    ret = permutations(chars, passlength)
    for comb in ret:
        # print(comb)
        counter += 1
    print("Number of combinations:", counter)
    print("--- %s seconds (Generation) ---" % (time.time() - start_timesp))
    return permutations(chars, passlength)
    pass


# def brut(chars, inp):
#     complete_list = []
#     for current in range(len(inp)):
#         a = [i for i in chars]
#         for y in range(current):
#             a = [x + i for i in chars for x in a]
#         complete_list = complete_list + a
#     print("Brute completed!")


inp = input("Введите текст для хеширования: ")
crc = zlib.crc32(inp.encode('UTF-8'))
print("Resulting crc32: ", crc)

chars = """~,!@"'#$%^&*()[]{}-<>/\.:;=+?abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"""
length = int(input('длина пароля?' + "\n"))
password = ''
for i in range(length):
    password += choice(chars)
print("Ваш пароль: ", password)
# generator(chars, len(password))
# brut3(chars, password)
brut5(chars, password)  # products from itertools, пока лучший вариант
# brut6(chars, password)  # combinations_with_replacements from itertools
# brut4(chars, password)  # set, проигрывает 5-ому (иногда больше пол минуты)

# brut4(chars, password)    # parasha
