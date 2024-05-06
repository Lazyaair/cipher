import tools_func as tf
import numpy as np


class AES_CBC:
    def __init__(self, key: np.ndarray, iv: np.ndarray):
        self.key = key
        self.iv = iv

    def encrypt(self, msg: bytes) -> bytes:
        block_list = tf.padding(msg)
        print(block_list)
        print(tf.tran_de(block_list))
        num = len(block_list)
        for i in range(num):
            if 'first' not in locals():
                block_list[i] = self.iv ^ block_list[i]
                block_list[i] = tf.encrypt_block(block_list[i], self.key.copy())
                first = True
            else:
                block_list[i] = block_list[i - 1] ^ block_list[i]
                block_list[i] = tf.encrypt_block(block_list[i], self.key.copy())
        print(block_list)
        return tf.tran_en(block_list)

    def decrypt(self, cipher: bytes) -> str:
        cipher_list = tf.padding(cipher, is_decrypt=True)
        print(cipher_list)
        num = len(cipher_list)
        msg_list = list()
        for i in range(num):
            if 'first' not in locals():
                msg_list.append(self.iv ^ tf.decrypt_block(cipher_list[i], self.key.copy()))
                first = True
            else:
                msg_list.append(cipher_list[i - 1] ^ tf.decrypt_block(cipher_list[i], self.key.copy()))
        print(msg_list)
        msg = tf.tran_de(msg_list)
        return msg


if __name__ == '__main__':
    aes = AES_CBC(
        np.array([
            [0x2b, 0x28, 0xab, 0x09],
            [0x7e, 0xae, 0xf7, 0xcf],
            [0x15, 0xd2, 0x15, 0x4f],
            [0x16, 0xa6, 0x88, 0x3c]
        ], dtype=np.uint8),
        np.array([
            [0x2b, 0x28, 0xab, 0x09],
            [0x7e, 0xae, 0x77, 0xcf],
            [0x15, 0xd2, 0x15, 0x4f],
            [0x16, 0x44, 0x88, 0x3c]
        ], dtype=np.uint8)
    )
    s = aes.encrypt('ninsci1d1212ddsafvgq34guansi'.encode())
    print(s)
    print(aes.decrypt(s))
