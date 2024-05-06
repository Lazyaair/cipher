import numpy as np
import pickle
import tools_func as tf
if __name__ == '__main__':
    s = '年乃是的亲离开南非w老夫发12'
    s = tf.padding(s.encode())
    # padding_num = -int(s[-1][-1][-1])
    # t_bytes = list()
    # for i in s:
    #     t_bytes.append(i.tobytes())
    # t_bytes = b''.join(t_bytes)[:padding_num]
    # print(tf.en_trans(s))
    print(tf.tran_de(s))
    # print(s)
    # s = s.decode()
    # print(s)
    # byte = s.encode()
    # p = list()
    # length = len(byte)
    # r = length % 16
    # print(r)
    # for i in range(length // 16):
    #     p.append(list(byte[i * 16:(i + 1) * 16]))
    # pb = list(byte[length - r:] + (16 - r) * (16-r).to_bytes(1,byteorder='big'))
    # print(pb)
    # p.append(pb)
    # a = np.array(p)
    # print(a.shape)
    #
    # a = np.array([
    #     [0xc9, 0x7c, 0x77, 0x7b],
    #     [0x6e, 0x6b, 0x6f, 0xc5],
    #     [0x46, 0x01, 0x67, 0x2b],
    #     [0xa6, 0xd7, 0xab, 0x76]
    # ])
    # print(a)
    # print(tf.byte_substitution(a, True))
    # print(tf.row_shift(a, True))
    # print(tf.mix_confusion(a))
    # m = np.array([
    #     [0x02, 0x03, 0x01, 0x01],
    #     [0x01, 0x02, 0x03, 0x01],
    #     [0x01, 0x01, 0x02, 0x03],
    #     [0x03, 0x01, 0x01, 0x02]
    # ])
    # print(tf.key_extend(m)[0])
    # b = np.array([
    #     [0xd4],
    #     [0xbf],
    #     [0x5d],
    #     [0x30]
    # ])
    # temp = np.empty(shape=(4, 1))
    # for i in range(4):
    #     for j in range(1):
    #         temp[i][j] = 0x00
    #         for k in range(4):
    #             temp[i][j] = int(temp[i][j]) ^ tf.dot(m[i][k], b[k][j])
    # print(temp)
    # print(m@b)
    a = np.array([
        [0x32, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x98, 0x07],
        [0xa8, 0x8d, 0xa2, 0x34]
    ], dtype=np.uint8)

    m = np.array([
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ], dtype=np.uint8)

    n = np.array([
        [0x2b, 0x28, 0xbb, 0x09],
        [0x7e, 0xee, 0xf7, 0xcf],
        [0x55, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ], dtype=np.uint8)
    # 加密
    print(a, '明文')
    tf.key_extend(m)
    a = tf.round_key_plus(a)
    # print(a, '第0轮')
    for i in range(9):
        a = tf.normal_round(a)
        # print(a, f'第{i+1}轮')
    a = tf.last_round(a)
    print(a, '第10轮')
    # print(tf.Round, tf.R)

    print('==========================================')
    # 解密
    print(a, '密文')
    a = tf.round_key_plus(a, reverse=True)
    # print(a, '第0轮')
    for i in range(9):
        a = tf.normal_round_reverse(a)
        # print(a, f'第{i+1}轮')
    a = tf.last_round_reverse(a)
    print(a, '第10轮')
    print(a, '明文')
    # print(tf.Round, tf.R)
    #
    # print(a)
    #
    # # 加密
    # a = tf.encrypt_block(a, m.copy())
    # print(a)
    # b = tf.encrypt_block(a, n.copy())
    # print(b)
    # # 解密
    # a = tf.decrypt_block(a, m.copy())
    # print(a)
    # b = tf.decrypt_block(b, n.copy())
    # print(b)
