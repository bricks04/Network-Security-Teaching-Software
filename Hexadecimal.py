e = 'dc99'
d = '1de5bb962fc1e79a820060484a18f989'
n = 'c9e9b28ce1f8f4cede3f0ab0bffc00a7'

e = int(e, 16)
d = int(d, 16)
n = int(n, 16)

e = 56473
d = 39740452567967507704776370563730438537
n = 268388253751594004171988248898146402471

import hashlib

message = 'Henry is'
#encrypt message
message = 'Henry is'.encode()
#print(message)
string = message.decode()
#print(string)
hex_seq = message.hex()
#print(hex_seq)

message_obj = hashlib.md5(b'Henry is')
print(message_obj)

M = '48656e7279206973207265746172646f'

M = int(M, 16)

M = 96231077813779758536241542276807025775

cipher_n = pow(M, e, n)

cipher = hex(cipher_n)

C = int(cipher, 16)

N = pow(C, d, n)

message_hex2 = hex(N)

message_obj2 = bytes.fromhex(message_hex2[2:])

message2 = message_obj2.decode()
                            
