import zlib
from random import choice
import time

def shift_left(input):
    result = input << 0x10
    if result > 0xffffffffffffffff:
        result = result & 0xffffffffffffffff
    else:
        result = result

    return result


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


def brutforce(chars, correctpass):
    wrongPasswords = []  # В этот список будут добавляться уже подобранные пароли, чтобы не повторяться
    password = ""  # В эту переменную будет записываться сгенерированный пароль,  и, если он ложный, пойдет в wrongPassword
    run = True

    while run:
        password = ""

        for i in range(length):
            password += random.choice(chars)

        if password not in wrongPasswords:
            if password != correctpass:
                # print(password)
                wrongPasswords.append(password)
            else:
                run = False
                break
    print("Password cracked):", password)


def brut3(chars, inputpassword):

    start_time = time.time()
    wrongPasswords = set()

    while True:
        password = ''
        for i in range(len(inputpassword)):
            password += choice(chars)

        if password not in wrongPasswords:
            if password != inputpassword:
                wrongPasswords.add(password)
            else:
                break

    print(password + " is correct")
    print("--- %s seconds ---" % (time.time() - start_time))


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
# brutforce(chars, password)
brut3(chars, password)
