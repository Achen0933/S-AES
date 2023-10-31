from encryption import encryption
from decryption import decryption


def CBC_encryption(plain, key):
    iv = "1111000010100101"
    cipher = []
    plain0 = []
    for i in range(int(len(plain)/16)):
        plain0.append(bin(int(iv, 2) ^ int(plain[16*i:16*(i+1)], 2))[2:].zfill(16))
        cipher.append(encryption(plain0[i], key))
        if len(cipher) !=0:
            iv = cipher[-1]
    #print("".join(cipher))
    return "".join(cipher)


def CBC_decryption(cipher, key):
    iv = "1111000010100101"
    plain = []
    cipher0 = []
    for i in range(int(len(cipher)/16)):
        cipher0.append(decryption(cipher[i*16:16*(i+1)], key))
        plain.append(bin(int(iv, 2)^int(cipher0[i], 2))[2:].zfill(16))
        iv = cipher[i*16:16*(i+1)]
    #print("".join(plain))
    return "".join(plain)


print("CBC模式加密：")
print("请输入明文：", end="")
plaintext = input()
print("请输入16位二进制密钥：", end="")
key = input()
ciphertext = CBC_encryption(plaintext, key)
print("本次加密的密文为：", ciphertext)
#print(CBC_encryption("10101010010101010010101001001010", "1111000010100101"))

print("\nCBC模式解密：")
print("请输入密文：", end="")
ciphertext = input()
print("请输入16位二进制密钥：", end="")
key = input()
plaintext = CBC_decryption(ciphertext, key)
print("本次解密的明文为：", plaintext)
#print(CBC_decryption("11101000011011011111000101010000", "1111000010100101"))

print("请输入篡改后的密文：", end="")
change_ciphertext = input()
change_plaintext = CBC_decryption(change_ciphertext, key)
print("修改后解密的明文为：", change_plaintext)

if plaintext != change_plaintext:
    print("可见，篡改密文后的解密结果和原来不一致。")

