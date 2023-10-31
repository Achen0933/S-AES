from encryption import encryption
from decryption import decryption


def double_encryption(plain,key):
    if len(key) > 8:
        key = hex(int(key, 2))[2:].upper()
    k1 = key[:4]
    k2 = key[-4:]
    mid = encryption(plain, k1)
    dciphertext = encryption(mid, k2)
    return dciphertext


def double_decryption(cipher, key):
    if len(key) > 8:
        key = hex(int(key, 2))[2:].upper()
    k1 = key[:4]
    k2 = key[-4:]
    mid = decryption(cipher, k2)
    dplaintext = decryption(mid, k1)
    return dplaintext


print("二重加密：")
print("请输入16位二进制明文或4位十六进制明文：", end="")
plaintext = input()
print("请输入32位二进制密钥或8位十六进制密钥：", end="")
key = input()
ciphertext = double_encryption(plaintext, key)
print("本次二重加密的密文为：", ciphertext)
#print(double_encryption("0000111100001111","00000000000000000111101110110010"))

print("\n二重解密：")
print("请输入16位二进制明文或4位十六进制密文：", end="")
ciphertext = input()
print("请输入32位二进制密钥或8位十六进制密钥：", end="")
key = input()
plaintext = double_decryption(ciphertext, key)
print("本次二重解密的明文为：", plaintext)
#print(double_decryption("1001110100000000","00000000000000000111101110110010"))



