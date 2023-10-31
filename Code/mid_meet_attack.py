from encryption import encryption
from decryption import decryption

def double_encryption(plain,key):
    if len(key) > 8:
        key = hex(int(key, 2))[2:].upper()
    k1 = key[:4]
    k2 = key[-4:]
    mid = encryption(plain, k1)
    dciphertext = encryption(mid, k2)
    return mid,dciphertext


def double_decryption(cipher, key):
    if len(key) > 8:
        key = hex(int(key, 2))[2:].upper()
    k1 = key[:4]
    k2 = key[-4:]
    mid = decryption(cipher, k2)
    dplaintext = decryption(mid, k1)
    return mid,dplaintext


def mid_meet_attack(known_plaintext, known_ciphertext):
      key = []
      keynum = 0
      for k1_guess in range(65536):  # 16位二进制字符串
        k1_bin = format(k1_guess, '016b')
        #print(k1_bin)
        for k2_guess in range(65536):  # 16位二进制字符串
            k2_bin = format(k2_guess, '016b')
            #print("k2",k2_bin)
            mid1, dciphertext = double_encryption(known_plaintext, k1_bin+k2_bin)
            mid2, dplaintext = double_decryption(known_ciphertext, k1_bin+k2_bin)
            if mid1 == mid2:
                keynum = keynum + 1
                key.append(k1_bin + k2_bin)
                print(keynum,key)

      return keynum, key


# 用已知的明文-密文对调用攻击函数
known_plaintext = "0000111100001111"
known_ciphertext = "1001110100000000"
possible_keynum, possible_keys = mid_meet_attack(known_plaintext, known_ciphertext)
print("Possible keynum:", possible_keynum)
print("Possible keys:", possible_keys)
