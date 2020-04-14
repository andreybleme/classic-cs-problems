from secrets import token_bytes
from typing import Tuple

def random_key(length: int):
  # generate random bytes
  tb: bytes = token_bytes(length)
  # convert bytes into chain of bits
  return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
  original_bytes: bytes = original.encode()
  dummy: int = random_key(len(original_bytes))
  # big for bigendian
  original_key: int = int.from_bytes(original_bytes, "big")
  # XOR operation
  encrypted: int = original_key ^ dummy
  return dummy, encrypted

def decrypt(key1: int, key2: int):
  decrypted: int = key1 ^ key2
  # add 7 to avoid 'off-by-one' errors when dividing by 8
  temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
  return temp.decode()

if __name__ == "__main__":
  key1, key2 = encrypt("Hello andreybleme")
  print("key1: {}, key2: {}".format(key1, key2))
  result: str = decrypt(key1, key2)
  print(result)