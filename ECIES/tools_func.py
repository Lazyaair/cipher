def int_to_binary(k):
    # 将整数转换为二进制字符串
    binary_str = bin(k)[2:]
    binary_slice = [0] + [int(c) for c in binary_str]

    # 转换为改进的二进制序列
    length = len(binary_slice)
    binary_seq = [0 for _ in range(length)]
    len_zero = 0
    for i in range(length - 1, -1, -1):
        if binary_slice[i] == 1:
            len_zero += 1
            binary_seq[i] = 1
            continue
        else:
            if len_zero > 1:
                binary_seq[i] = 1
                for j in range(1, len_zero):
                    binary_seq[i + j] = 0
                binary_seq[i + len_zero] = -1
                len_zero = 1
            else:
                len_zero = 0

    return binary_seq


def str2list(s: str) -> list:
    return [ord(i) for i in s]


def list2str(l: list) -> str:
    sl = [chr(i) for i in l]
    return ''.join(sl)


# 示例用法
k = 23
print(bin(k)[2:])
binary_sequence = int_to_binary(k)
print(binary_sequence)
l = str2list('6ni号')
print(l)
s = list2str(l)
print(s)

print(int("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF",16)%4)
