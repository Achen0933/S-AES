from encryption import encryption
from decryption import decryption

def encryption_ascii(plaintext, key):
    # 将 ASCII 字符串转换为二进制
    binary_plaintext = ''.join(format(ord(char), '08b') for char in plaintext)
    # 将二进制字符串分成八位一组
    blocks = [binary_plaintext[i:i + 16] for i in range(0, len(binary_plaintext), 16)]
    ciphertext = []
    for block in blocks:
        cipher = encryption(block, key)
        ciphertext.append(cipher)
    ciphertext = ''.join(ciphertext)
    # 如果需要，可以将二进制结果转换回 ASCII 字符串
    ciphertext_ascii = ''.join(chr(int(ciphertext[i:i + 8], 2)) for i in range(0, len(ciphertext), 8))
    return ciphertext_ascii

def decryption_ascii(ciphertext, key):
    # 将 ASCII 字符串转换为二进制
    binary_ciphertext = ''.join(format(ord(char), '08b') for char in ciphertext)
    # 将二进制字符串分成十六位一组
    blocks = [binary_ciphertext[i:i + 16] for i in range(0, len(binary_ciphertext), 16)]
    plaintext = []
    for block in blocks:
        plain = decryption(block, key)
        plaintext.append(plain)
    plaintext = ''.join(plaintext)
    # 如果需要，可以将二进制结果转换回 ASCII 字符串
    plaintext_ascii = ''.join(chr(int(plaintext[i:i + 8], 2)) for i in range(0, len(plaintext), 8))
    return plaintext_ascii
