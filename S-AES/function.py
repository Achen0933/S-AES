import numpy as np


def h_b(input):
    binary_key = bin(int(input, 16))
    key = binary_key[2:]
    key = key.zfill(16)
    return key


# 轮密钥加
def key_round(plain, key):
    result = bin(int(plain, 2) ^ int(key, 2))[2:].zfill(16)
    return result


def S_box(input):
    box = np.array([['9', '4', 'A', 'B'],
                    ['D', '1', '8', '5'],
                    ['6', '2', '0', '3'],
                    ['C', 'E', 'F', '7']])
    a1 = int(input[:2], 2)
    a2 = int(input[2: 4], 2)
    a3 = int(input[4: 6], 2)
    a4 = int(input[6: 8], 2)
    b1 = box[a1][a2]
    b2 = box[a3][a4]
    b1 = bin(int(b1, 16))[2:].zfill(4)
    b2 = bin(int(b2, 16))[2:].zfill(4)
    return b1 + b2


# 字节代替
def substitution(input):
    #b_input = h_b(input)
    a1 = input[:8]
    a2 = input[-8:]
    b1 = S_box(a1)
    b2 = S_box(a2)
    return b1 + b2


def IS_box(input):
    box = np.array([['A', '5', '9', 'B'],
                    ['1', '7', '8', 'F'],
                    ['6', '0', '2', '3'],
                    ['C', '4', 'D', 'E']])
    a1 = int(input[:2], 2)
    a2 = int(input[2: 4], 2)
    a3 = int(input[4: 6], 2)
    a4 = int(input[6: 8], 2)
    b1 = box[a1][a2]
    b2 = box[a3][a4]
    b1 = bin(int(b1, 16))[2:].zfill(4)
    b2 = bin(int(b2, 16))[2:].zfill(4)
    return b1 + b2


# 逆字节代替
def isubstitution(input):
    #b_input = h_b(input)
    a1 = input[:8]
    a2 = input[-8:]
    b1 = IS_box(a1)
    b2 = IS_box(a2)
    return b1 + b2


# 行替换
def linedisplay(input):
    output = input[0:4]+input[-4:]+input[8:12]+input[4:8]
    return output


def column_mix(plain):
    # 列混淆矩阵
    mix = np.array([[1, 4],
                    [4, 1]])
    plain = hex(int(plain, 2))[2:].upper().zfill(4)
    plain0 = np.array([[plain[0], plain[2]],
                       [plain[1], plain[3]]])
    #print(plain0)
    GF4 = ['0', '4', '8', 'C', '3', '7', 'B', 'F', '6', '2', 'E', 'A', '5', '1', 'D', '9' ]
    a = bin(int(plain0[0][0], 16) ^ int(GF4[int(plain0[1][0], 16)], 16))[2:].zfill(4)
    b = bin(int(GF4[int(plain0[0][0], 16)], 16) ^ int(plain0[1][0], 16))[2:].zfill(4)
    c = bin(int(plain0[0][1], 16) ^ int(GF4[int(plain0[1][1], 16)], 16))[2:].zfill(4)
    d = bin(int(GF4[int(plain0[0][1], 16)], 16) ^ int(plain0[1][1], 16))[2:].zfill(4)
    return a + b + c + d


def icolumn_mix(cipher):
    # 逆列混淆矩阵
    mix = np.array([[9, 2],
                    [2, 9]])
    cipher = hex(int(cipher, 2))[2:].upper().zfill(4)
    cipher0 = np.array([[cipher[0], cipher[2]],
                       [cipher[1], cipher[3]]])
    GF2 = ['0', '2', '4', '6', '8', 'A', 'C', 'E', '3', '1', '7', '5', 'B', '9', 'F', 'D']
    GF9 = ['0', '9', '1', '8', '2', 'B', '3', 'A', '4', 'D', '5', 'C', '6', 'F', '7', 'E']
    a = bin(int(GF9[int(cipher0[0][0], 16)], 16) ^ int(GF2[int(cipher0[1][0], 16)], 16))[2:].zfill(4)
    b = bin(int(GF2[int(cipher0[0][0], 16)], 16) ^ int(GF9[int(cipher0[1][0], 16)], 16))[2:].zfill(4)
    c = bin(int(GF9[int(cipher0[0][1], 16)], 16) ^ int(GF2[int(cipher0[1][1], 16)], 16))[2:].zfill(4)
    d = bin(int(GF2[int(cipher0[0][1], 16)], 16) ^ int(GF9[int(cipher0[1][1], 16)], 16))[2:].zfill(4)
    return a + b + c + d


