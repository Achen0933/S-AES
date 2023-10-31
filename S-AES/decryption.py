from key import key
from function import h_b,key_round,isubstitution,linedisplay,icolumn_mix

# 实例化key类
key = key()


def decryption(ciphertext, key0):
    # 如果密文为十六进制字符串，转换为16位二进制字符串
    if len(ciphertext) < 16:
        ciphertext = h_b(ciphertext)
    #print("ciphertext:", ciphertext)

    # 如果密钥为16位二进制字符串，转换为4位十六进制字符串
    if len(key0) > 4:
        key0 = hex(int(key0, 2))[2:].upper()
    #print("key0:", key0)
    # 密钥扩展，输入为十六进制字符串，输出为三个16位二进制字符串
    w01, w23, w45 = key.key_expansion(key0)
    #print("w01,w02,w03:", w01, w23, w45)

    # 以下操作输入输出全部为16位二进制字符串
    # 进行第一次轮密钥加
    step0_round = key_round(ciphertext, w45)

    # 第一轮
    step1_dis = linedisplay(step0_round)
    step2_isub = isubstitution(step1_dis)
    step3_round = key_round(step2_isub, w23)
    step4_imix = icolumn_mix(step3_round)

    # 第二轮
    step5_dis = linedisplay(step4_imix)
    step6_isub = isubstitution(step5_dis)
    step7_round = key_round(step6_isub, w01)

    # 输出明文
    plaintext = step7_round
    return plaintext
