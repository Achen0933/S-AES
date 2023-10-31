import numpy as np


class key:
    def h_b(self, key0):
        binary_key = bin(int(key0, 16))
        key = binary_key[2:]
        key = key.zfill(16)
        return key

    def RotNib(self, key0):
        key = key0[-4:] + key0[:4]
        return key

    def S_box(self, key0):
        box = np.array([['9', '4', 'A', 'B'],
                        ['D', '1', '8', '5'],
                        ['6', '2', '0', '3'],
                        ['C', 'E', 'F', '7']])
        a1 = int(key0[:2], 2)
        a2 = int(key0[2: 4], 2)
        a3 = int(key0[4: 6], 2)
        a4 = int(key0[6: 8], 2)
        b1 = box[a1][a2]
        b2 = box[a3][a4]
        b1 = bin(int(b1, 16))[2:].zfill(4)
        b2 = bin(int(b2, 16))[2:].zfill(4)
        return b1 + b2

    def xor(self, a, b):
        a = int(a, 2)
        b = int(b, 2)
        return bin(a ^ b)[2:].zfill(8)

    def key_expansion(self, key0):
        rcon1 = "10000000"
        rcon2 = "00110000"
        # 先转换为16位的二进制
        key1 = self.h_b(key0)
        skey0 = key1[:8]
        skey1 = key1[-8:]
        skey2 = self.xor(skey0, self.xor(rcon1, self.S_box(self.RotNib(skey1))))
        skey3 = self.xor(skey2, skey1)
        skey4 = self.xor(skey2, self.xor(rcon2, self.S_box(self.RotNib(skey3))))
        skey5 = self.xor(skey4, skey3)
        return skey0 + skey1, skey2 + skey3, skey4 + skey5


#print(key().key_expansion("2D55"))
