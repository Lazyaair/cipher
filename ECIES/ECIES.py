import secrets
from typing import Optional


# class EllipticCurve:
#     def __init__(self, p, a, b):
#         self.p = int(p, 16)
#         self.a = int(a, 16)
#         self.b = int(b, 16)
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def is_infinity(self):
#         return self.x is None and self.y is None
#
# def inverse_mod(k, p):
#     if k == 0:
#         raise ZeroDivisionError('division by zero')
#     return pow(k, p - 2, p)
#
# def point_addition(curve, P, Q):
#     if P.is_infinity():
#         return Q
#     if Q.is_infinity():
#         return P
#     if P.x == Q.x and P.y != Q.y:
#         return Point(None, None)
#
#     if P == Q:
#         m = (3 * P.x * P.x + curve.a) * inverse_mod(2 * P.y, curve.p) % curve.p
#     else:
#         m = (Q.y - P.y) * inverse_mod(Q.x - P.x, curve.p) % curve.p
#
#     x_r = (m * m - P.x - Q.x) % curve.p
#     y_r = (m * (P.x - x_r) - P.y) % curve.p
#     return Point(x_r, y_r)
#
# def point_multiplication(curve, P, n):
#     R = Point(None, None)
#     N = P
#     while n > 0:
#         if n & 1:
#             R = point_addition(curve, R, N)
#         N = point_addition(curve, N, N)
#         n >>= 1
#     return R
#
# def compress_point(P):
#     return P.x, P.y % 2
#
# def tonelli_shanks(n, p):
#     assert legendre_symbol(n, p) == 1, "n is not a square (mod p)"
#     if p % 4 == 3:
#         return pow(n, (p + 1) // 4, p)
#     q, s = p - 1, 0
#     while q % 2 == 0:
#         q //= 2
#         s += 1
#     z = next(z for z in range(2, p) if legendre_symbol(z, p) == -1)
#     m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
#     while t != 0 and t != 1:
#         t2i, i = t, 0
#         for i in range(1, m):
#             t2i = pow(t2i, 2, p)
#             if t2i == 1:
#                 break
#         b = pow(c, 1 << (m - i - 1), p)
#         m, c, t, r = i, pow(b, 2, p), t * pow(b, 2, p) % p, r * b % p
#     return r
#
# def legendre_symbol(a, p):
#     ls = pow(a, (p - 1) // 2, p)
#     return -1 if ls == p - 1 else ls
#
# def decompress_point(curve, x, y_bit):
#     alpha = (x * x * x + curve.a * x + curve.b) % curve.p
#     try:
#         beta = tonelli_shanks(alpha, curve.p)
#     except AssertionError:
#         raise ValueError("Square root computation failed.")
#     if beta % 2 != y_bit:
#         beta = curve.p - beta
#     return Point(x, beta)
#
# def generate_keypair(curve, G, n):
#     private_key = secrets.randbelow(n)
#     public_key = point_multiplication(curve, G, private_key)
#     return private_key, public_key
#
# # 椭圆曲线参数
# p_hex = "FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF"
# a_hex = "FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC"
# b_hex = "28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93"
#
# curve = EllipticCurve(p_hex, a_hex, b_hex)
#
# # 基点 G 和阶 n
# G = Point(
#     int("32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7", 16),
#     int("BC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0", 16)
# )
# n = int("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123", 16)
#
# # 生成密钥对
# private_key, public_key = generate_keypair(curve, G, n)
# print("私钥:", hex(private_key))
# print("公钥: ({}, {})".format(hex(public_key.x), hex(public_key.y)))
#
# def encrypt(curve, G, public_key, message_point):
#     k = secrets.randbelow(n)
#     C1 = point_multiplication(curve, G, k)
#     kQ = point_multiplication(curve, public_key, k)
#     C2 = point_addition(curve, message_point, kQ)
#     return C1, C2
#
# def decrypt(curve, private_key, C1, C2):
#     kQ = point_multiplication(curve, C1, private_key)
#     M = point_addition(curve, C2, Point(kQ.x, -kQ.y % curve.p))
#     return M
#
# # 示例消息点
# message_point = Point(
#     15,
#
# )
#
# # 加密消息
# C1, C2 = encrypt(curve, G, public_key, message_point)
# print("加密后的消息:", C1, C2)
#
# # 压缩和解压缩点
# compressed_C1 = compress_point(C1)
# compressed_C2 = compress_point(C2)
#
# print("压缩后的C1:", compressed_C1)
# print("压缩后的C2:", compressed_C2)
#
# decompressed_C1 = decompress_point(curve, *compressed_C1)
# decompressed_C2 = decompress_point(curve, *compressed_C2)
#
# print("解压缩后的C1:", decompressed_C1)
# print("解压缩后的C2:", decompressed_C2)
#
# # 解密消息
# decrypted_point = decrypt(curve, private_key, decompressed_C1, decompressed_C2)
# print("解密后的消息:", decrypted_point)

class EllipticCurve:
    def __init__(self, p, a, b):
        self.p = int(p, 16)
        self.a = int(a, 16)
        self.b = int(b, 16)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({hex(self.x)}, {hex(self.y)})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def is_infinity(self):
        return self.x is None and self.y is None


"""
// SM2椭圆曲线公钥密码算法推荐曲线参数
// 推荐使用素数域256位椭圆曲线。
// 椭圆曲线方程：y^2 = x^3 + ax + b。
// 曲线参数：
// p=FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF 00000000 FFFFFFFF FFFFFFFF
// a=FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF 00000000 FFFFFFFF FFFFFFFC
// b=28E9FA9E 9D9F5E34 4D5A9E4B CF6509A7 F39789F5 15AB8F92 DDBCBD41 4D940E93
// n=FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF 7203DF6B 21C6052B 53BBF409 39D54123
// Gx=32C4AE2C 1F198119 5F990446 6A39C994 8FE30BBF F2660BE1 715A4589 334C74C7
// Gy=BC3736A2 F4F6779C 59BDCEE3 6B692153 D0A9877C C62A4740 02DF32E5 2139F0A0
"""
# 椭圆曲线参数
p_hex = "FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF"
a_hex = "FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC"
b_hex = "28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93"
# 定义椭圆曲线基点 G 和阶 n
G = Point(
    int("32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7", 16),
    int("BC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0", 16)
)
n = int("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123", 16)


def point_addition(curve, P, Q) -> Optional[Point]:
    if P is None:
        return Q
    if Q is None:
        return P
    if P.x == Q.x and P.y != Q.y:
        return None
    if P == Q:
        m = (3 * P.x * P.x + curve.a) * pow(2 * P.y, -1, curve.p) % curve.p
    else:
        m = (Q.y - P.y) * pow(Q.x - P.x, -1, curve.p) % curve.p
    x_r = (m * m - P.x - Q.x) % curve.p
    y_r = (m * (P.x - x_r) - P.y) % curve.p
    return Point(x_r, y_r)


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


def point_multiplication(curve, P, n):
    r = None
    # for i in range(n.bit_length()):
    #     if n & (1 << i):
    #         R = point_addition(curve, R, P)
    #     P = point_addition(curve, P, P)
    binary_seq = int_to_binary(n)
    # print(binary_seq)
    length = len(binary_seq)
    for i in range(length - 1, -1, -1):
        if binary_seq[i] == 1:
            r = point_addition(curve, r, P)
        elif binary_seq[i] == -1:
            r = point_addition(curve, r, Point(P.x, (curve.p - P.y) % curve.p))
        else:
            P = point_addition(curve, P, P)
    return r


# 生成密钥对
def generate_keypair(curve, G, n):
    private_key = secrets.randbelow(n)
    public_key = point_multiplication(curve, G, private_key)
    return private_key, public_key


def compress_point(P):
    return Point(P.x, P.y % 2)


def decompress_point(curve, p: Point):
    alpha = (p.x * p.x * p.x + curve.a * p.x + curve.b) % curve.p
    beta = pow(alpha, (curve.p + 1) // 4, curve.p)
    if beta % 2 == p.y:
        return Point(p.x, beta)
    else:
        return Point(p.x, curve.p - beta)


def encrypt(curve, G, public_key, message):
    k = secrets.randbelow(n)
    C1 = point_multiplication(curve, G, k)
    C1 = compress_point(C1)
    kQ = point_multiplication(curve, public_key, k)
    C2 = kQ.x * message % curve.p
    return C1, C2


def decrypt(curve, private_key, C1, C2):
    C1 = decompress_point(curve, C1)
    kQ = point_multiplication(curve, C1, private_key)
    M = C2 * pow(kQ.x, -1, curve.p) % curve.p
    return M


# 使用前面定义的椭圆曲线参数
curve0 = EllipticCurve(p_hex, a_hex, b_hex)

# 生成密钥对
pri_key, pub_key = generate_keypair(curve0, G, n)
print("私钥:", hex(pri_key))
print("公钥: ({}, {})".format(hex(pub_key.x), hex(pub_key.y)))

# 测试加密和解密
# message_point = Point(10, 15)  # 示例消息点
msg = 9919999
print("原始的消息:", msg)
c1, c2 = encrypt(curve0, G, pub_key, msg)
print("加密后的消息:", c1, hex(c2))

decrypted_point = decrypt(curve0, pri_key, c1, c2)
print("解密后的消息:", decrypted_point)
print('====================================================================================')


def str2list(S: str) -> list:
    return [ord(i) for i in S]


def list2str(L: list) -> str:
    sl = [chr(i) for i in L]
    return ''.join(sl)


msg_str = '我是2022212357,你是谁'
print(f'初始消息：{msg_str}')
print('======开始加密=====')
ml = str2list(msg_str)
sec_l = []
for i in ml:
    sec_l.append(tuple(encrypt(curve0, G, pub_key, i)))
print(f'密文列表：{sec_l}')
print('======开始解密=====')
plain_l = []
for i in sec_l:
    plain_l.append(decrypt(curve0, pri_key, i[0], i[1]))
print(f'明文列表：{plain_l}')
p = list2str(plain_l)
print(f'解密消息：{p}')
