from key import key
from function import h_b,key_round,substitution,linedisplay,column_mix

# 实例化key类
key = key()


def encryption(plaintext, key0):
    # 如果明文为4位十六进制字符串，转换为16位二进制字符串
    if len(plaintext) < 16:
        plaintext = h_b(plaintext)
    #print("plaintext:",plaintext)

    # 如果密钥为16位二进制字符串，转换为4位十六进制字符串
    if len(key0) > 4:
        key0 = hex(int(key0, 2))[2:].upper()
    #print("key0:",key0)
    # 密钥扩展，输入为十六进制字符串，输出为三个16位二进制字符串
    w01, w23, w45 = key.key_expansion(key0)
    #print("w01,w02,w03:",w01,w23,w45)

    # 以下操作输入输出全部为16位二进制字符串
    # 进行第一次轮密钥加
    step0_round = key_round(plaintext, w01)

    # 第一轮
    step1_sub = substitution(step0_round)
    step2_dis = linedisplay(step1_sub)
    step3_mix = column_mix(step2_dis)
    step4_round = key_round(step3_mix, w23)

    # 第二轮
    step5_sub = substitution(step4_round)
    step6_dis = linedisplay(step5_sub)
    step7_round = key_round(step6_dis, w45)

    # 输出密文
    ciphertext = step7_round
    return ciphertext




