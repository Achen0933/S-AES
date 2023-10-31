from encryption import encryption
from decryption import decryption


def tribble_encryption(plain, key):
    mid1 = encryption(plain, key[0:16])
    mid2 = encryption(mid1, key[16:32])
    out = encryption(mid2, key[0:16])
    return out


def tribble_decryption(cipher, key):
    mid1 = decryption(cipher, key[0:16])
    mid2 = decryption(mid1, key[16:32])
    out = decryption(mid2, key[0:16])
    return out

print("三重加密：")
print("请输入16位二进制明文或4位十六进制明文：", end="")
plaintext = input()
print("请输入32位二进制密钥：", end="")
key = input()
ciphertext = tribble_encryption(plaintext, key)
print("本次三重加密的密文为：", ciphertext)
#print(double_encryption("0000111100001111","00000000000000100101101010101010"))

print("\n三重解密：")
print("请输入16位二进制明文或4位十六进制密文：", end="")
ciphertext = input()
print("请输入32位二进制密钥：", end="")
key = input()
plaintext = tribble_decryption(ciphertext, key)
print("本次三重解密的明文为：", plaintext)
#print(double_decryption("1001110100000000","00000000000000100101101010101010"))